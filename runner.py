import argparse
import importlib

from framework.config import Config
from framework.log import Logger

config = Config()
logger = Logger()

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def main(args):

    entry = None
    
    # Black Myth Wukong
    if "bmwk" in config.env_short_name.lower():
        runner_module = importlib.import_module('framework.runner.bmwk_runner')
        entry = getattr(runner_module, 'entry')

    assert entry is not None, "Entry function is not defined in the environment module."

    # Run the entry
    entry(args)

def get_args_parser():
    parser = argparse.ArgumentParser("Action Execution Framework")
    parser.add_argument("--envConfig", type=str, default="./config/env_config_bmwk.json", help="The path to the environment config file")
    return parser

if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args()

    config.load_env_config(args.envConfig)
    config.set_fixed_seed()

    main(args)
