#! ./.venv/ python3

import sys

import logging
logger = logging.getLogger("main")

from __init__ import __version__
from .ui.app import NcLabsApp

class NcLabs():
    def __init__(self, args):
        super().__init__()
        
        self.__version__ = __version__
        
        sys.stdout.write(f"\33]0;NcLabs {self.__version__}\a")
        sys.stdout.flush()
        
        self.app = NcLabsApp()
        self.app.title = f"NcLabs - {__version__}{" [DEBUG]" if args.debug else ""}"
        self.app.run()
