import time
from typing import Tuple

from framework.config import Config
from framework.gameio.io_env import IOEnvironment
from framework.log import Logger
from framework import constants

config = Config()
logger = Logger()
io_env = IOEnvironment()

class GameManager():

    def __init__(
        self,
        env_name = config.env_name,
        ui_control = None,
    ):
        self.env_name = env_name
        self.env_short_name = config.env_short_name
        self.ui_control = ui_control

    def pause_game(self,
                   *args,
                   env_name=config.env_name,
                   ide_name=config.ide_name,
                   screen_type=constants.GENERAL_GAME_INTERFACE,
                   **kwargs):
        if screen_type==constants.PAUSE_INTERFACE:
            return False
        else:
            self.ui_control.pause_game(
                env_name=env_name,
                ide_name=ide_name,
                **kwargs
            )
            return True


    def unpause_game(self,
                     *args,
                     env_name=config.env_name,
                     ide_name=config.ide_name,
                     **kwargs):

        self.ui_control.unpause_game(
            env_name=env_name,
            ide_name=ide_name,
            **kwargs
        )
        return True


    def switch_to_game(self,
                       *args,
                       env_name=config.env_name,
                       ide_name=config.ide_name,
                       **kwargs):

        self.ui_control.switch_to_game(
            env_name=env_name,
            ide_name=ide_name,
            **kwargs
        )


    def capture_screen(self):
        tid = time.time()
        return self.ui_control.take_screenshot(tid)


    def cleanup_io(self):
        io_env.release_held_keys()
        io_env.release_held_buttons()
