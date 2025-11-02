#! ./.venv/ python3

""" NcLabs Program

NcLabs is a program that helps developers better navigate their various projects. 
It allows you to version your projects and manage them in a simple and intuitive way.
"""

import logging
try:  # Python 2.7+
    from logging.config import dictConfig
except ImportError as error:
    raise(f"Unable to import the module needed for logging. Check that your Python version is 2.7 or later.\n{error}")
    
import yaml
import argparse
import os

from __init__ import (
    __shortname__,
    __longname__,
    __version__
)
import utils._os
import utils.environment
import utils.pypixz_lite

checks = {"os": {"name": "OS", "function": lambda: utils._os.os_compatibility()},
          "env": {"name": "environment", "function": lambda: utils.environment.python_compatiblity()},
          "packages": {"name": "packages", "function": lambda: utils.pypixz_lite.install_requirements(os.path.abspath("../requirements.txt"), True)}}


def argparse_setup() -> argparse.Namespace:
    """argparse_setup Configures the argparse module.

    This function creates and configures an `argparse.ArgumentParser` object to
    manage the program's launch arguments.

    Returns:
        argparse.Namespace -- An object containing the parsed arguments.
    """
    
    parser = argparse.ArgumentParser(description=f"{__longname__} ({__version__})")
    parser.add_argument("-v", "--version", action="version", version=f"{__shortname__} - {__version__}")
    parser.add_argument("-u", "--update", action="store_true", help="update the program to the latest version")
    parser.add_argument("--skip-check", nargs="+", choices=["os", "env", "packages", "all"], help="pass the program launch checks")
    parser.add_argument("--debug", action="store_true", help="enable debug output")
    args = parser.parse_args()
    
    return parser, args


def logging_setup(args: argparse.Namespace) -> logging.Logger:
    """logging_setup Configure the logging system based on the passed arguments.

    This function initializes and adapts the behavior of the main logger based on
    the options and information provided.

    Arguments:
        args {argparse.Namespace} -- The parsed command line arguments.

    Returns:
        logging.Logger -- The configured logger instance.
    """
    logger = logging.getLogger("main")
    if args.debug:
        logger.setLevel(logging.DEBUG)
        
    for handler in logger.handlers:
        if getattr(handler, "baseFilename", "").endswith("debug.log"):
            handler.addFilter(lambda record: record.levelno == logging.DEBUG)
        
    return logger
    

if __name__ == "__main__":
    with open("NcLabs/cache/logging.yaml", "r") as file:
        config = yaml.safe_load(file)
        dictConfig(config)
        
    parser, args = argparse_setup()
    logger = logging_setup(args)

    skips = args.skip_check or []
    if "all" in skips:
        if skips and (len(skips) > 1 or skips[0] != "all"):
            parser.error("The 'all' argument must be the first and only choice after '--skip-check'.")
    
    for obj, data in checks.items():
        if obj not in skips and "all" not in skips:
            logger.debug(f"Running {data["name"]} compatibility check...")
            data["function"]()
        else:
            logger.warning(f"Skipping {data["name"]} compatibility check.")
            
    if args.update:
        import utils.update
        utils.update.update_program()
        exit()

    from core import NcLabs
    NcLabs(args)
