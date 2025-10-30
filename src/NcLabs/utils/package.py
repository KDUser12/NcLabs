#! ./.venv/ python3

import os

import logging
logger = logging.getLogger("main")
        
requirements_file = os.path.abspath("../requirements.txt")

def packages_install() -> None:
    if os.path.exists(requirements_file):
        print(True)