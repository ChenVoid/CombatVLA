import atexit
from typing import Any

from framework.utils.string_utils import replace_unsupported_chars
from framework.log import Logger
from framework.config import Config
from framework.environment import BMWKUIControl
from framework.gameio.io_env import IOEnvironment
from framework.gameio.game_manager import GameManager
from framework.log.logger import process_log_messages
from framework.provider import VideoRecordProvider
from framework.provider import VideoClipProvider

import pdb
import os

from call_api import call_combatvla
import cv2
import shutil
import numpy as np
import time
import re
import ast


config = Config()
logger = Logger()
io_env = IOEnvironment()
video_record = VideoRecordProvider()

class PipelineRunner():

    def __init__(self):
        # Init internal params
        self.set_internal_params()

    def set_internal_params(self, *args, **kwargs):
        self.ui_control = BMWKUIControl()
        self.gm = GameManager(ui_control=self.ui_control)

        # Init video provider
        self.video_clip = VideoClipProvider(gm=self.gm)
        self.call_combatvla = call_combatvla

    def pipeline_shutdown(self):
        self.gm.cleanup_io()
        video_record.finish_capture()
        log = process_log_messages(config.work_dir)
        with open(config.work_dir + '/logs/log.md', 'w', encoding='utf-8') as f:
            log = replace_unsupported_chars(log)
            f.write(log)
        logger.write('>>> Markdown generated.')
        logger.write('>>> Bye.')

    def sample_and_save_last_frames(self, video_path, output_dir, resize_dim=(1008, 560)):
        video_path = video_path.replace('\\', '/')
        os.makedirs(output_dir, exist_ok=True)
        
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Ensure there are at least 9 frames to sample
        temp_num_frame = 5
        if total_frames < temp_num_frame:
            temp_num_frame = 3
        
        # Calculate indices for the last 9 frames
        last_n_frames = np.arange(total_frames - temp_num_frame, total_frames)
        
        # Select 3 frames evenly from these 9 frames
        sample_indices = np.linspace(last_n_frames[0], last_n_frames[-1], 3, dtype=int)
        
        for i, frame_idx in enumerate(sample_indices):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            
            ret, frame = cap.read()
            if not ret:
                print(f"Failed to capture frame at index {frame_idx}.")
                continue
            
            resized_frame = cv2.resize(frame, resize_dim)
            output_file_path = os.path.join(output_dir, f"frame_{i+1}.jpg")
            cv2.imwrite(output_file_path, resized_frame)
        
        cap.release()

    
    def extract_dict_from_string(self, input_string):
        match = re.search(r'{.*}', input_string)
        if match:
            dict_str = match.group(0)
            try:
                result_dict = ast.literal_eval(dict_str)
                return result_dict
            except ValueError:
                print("Failed to transfer the strings.")
                return None
        else:
            print("Not found proper dict structure.")
            return None

    def action_execution(self, action_dict):
        actions = action_dict['actions']

        for action in actions:
            if action['type'] == 'keyboard':
                key = action["key"]
                if action['action'] == 'hold':
                    io_env.key_hold(key, action['duration'])
                elif action['action'] == 'press':
                    io_env.key_press(f"{key}, {key}")

            elif action['type'] == 'mouse':
                if action['action'] == 'hold':
                    io_env.mouse_hold(button=io_env.RIGHT_MOUSE_BUTTON, duration=action['duration'])
                elif action['action'] == 'press':
                    io_env.mouse_click_button(button=io_env.LEFT_MOUSE_BUTTON, clicks=2)
 

    def run(self):
        # Initiate the parameters
        success = False

        # Switch to game
        self.gm.switch_to_game()

        # Start video recording
        video_record.start_capture()

        # Initiate screen shot path and video clip path
        self.video_clip(init = True)
        self.gm.pause_game()

        # Start the pipeline
        step = 0
        last_video_clip_path = ""
        while not success:
            try:
                start_time = time.time()
                if len(last_video_clip_path) == 0:
                    video_path = os.path.join("./runs", os.listdir("./runs")[0], "video_splits", "video_-00001.mp4")
                else:
                    video_path = last_video_clip_path

                output_dir = os.path.join("./runs", os.listdir("./runs")[0], "frames")
                if os.path.exists(output_dir):
                    shutil.rmtree(output_dir)
                os.makedirs(output_dir)

                self.sample_and_save_last_frames(video_path, output_dir)

                frame_list = os.listdir(output_dir)
                image_path_list = []
                for frame_name in frame_list:
                    image_path_list.append(os.path.join(output_dir, frame_name))

                action_str = self.call_combatvla(image_path_list)

                action_dict = self.extract_dict_from_string(action_str)
                print(action_dict)
                end_time = time.time()

                print(f"Duration is {end_time - start_time}s")

                print("open")
                start_frame_id = video_record.get_current_frame_id()
                self.action_execution(action_dict)
                end_frame_id = video_record.get_current_frame_id()
                print("close")

                last_video_clip_path = video_record.get_video(start_frame_id, end_frame_id)

                step += 1

                if step > config.max_steps:
                    logger.write('Max steps reached, exiting.')
                    break

            except KeyboardInterrupt:
                logger.write('KeyboardInterrupt Ctrl+C detected, exiting.')
                self.pipeline_shutdown()
                break

        self.pipeline_shutdown()


def exit_cleanup(runner):
    logger.write("Exiting pipeline.")
    runner.pipeline_shutdown()


def entry(args):
    pipelineRunner = PipelineRunner()
    atexit.register(exit_cleanup, pipelineRunner)
    pipelineRunner.run()
