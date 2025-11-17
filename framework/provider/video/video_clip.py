from typing import Any, Dict
import time

from framework.provider import BaseProvider
from framework.log import Logger
from framework.provider import VideoRecordProvider

logger = Logger()
video_record = VideoRecordProvider()

class VideoClipProvider(BaseProvider):
    def __init__(self, gm):
        super(VideoClipProvider, self).__init__()
        self.gm = gm

    @BaseProvider.write
    def __call__(self,
                 *args,
                 init = False,
                 **kwargs):

        if init:
            start_frame_id = video_record.get_current_frame_id()
            screen_shot_path = self.gm.capture_screen()
            time.sleep(2)
            end_frame_id = video_record.get_current_frame_id()
            video_clip_path = video_record.get_video(start_frame_id, end_frame_id)

            logger.write(f"Initiate video clip path from the screen shot by frame id ({start_frame_id}, {end_frame_id}).")

            res_params = {
                "video_clip_path": video_clip_path,
                "start_frame_id": start_frame_id,
                "end_frame_id": end_frame_id,
                "screen_shot_path": screen_shot_path,
            }


        return res_params