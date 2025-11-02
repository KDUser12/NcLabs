#! ./.venv/ python3

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Input, Label
import platform
import sys

import logging
logger = logging.getLogger("main")

from __init__ import __version__


class NcLabsApp(App):
    """NcLabs Textual interface with Vim-style layout."""
    CSS_PATH = "style.tcss"
    
    BINDINGS = [
        ("ctrl+c", "quit", "Quit NcLabs"),
    ]
    def __init__(self):
        super().__init__()
        
        self.__version__ = __version__
        self.os = platform.system()
        self.environment_version = '.'.join(map(str, sys.version_info[:3]))
        self.project_name = None
    
    def on_mount(self) -> None:
        self.theme = "flexoki"

    def compose(self) -> ComposeResult:
        yield Container(
            Static(
                f"""\
NcLabs - {self.__version__} [Python {self.environment_version}] on {self.os}
For more information enter "help", "license" or "credit".

type    :help[dim]<enter>[/dim]    list of available commands
type    :q[dim]<enter>[/dim]       to exit                   

type    :changelogs[dim]<enter>[/dim] to see changes in {self.__version__}
""",
                id="welcome",
            )
        )
        yield Label(f"{"\[Project Name]" if not self.project_name else ""}", id="footer")
        yield Input(placeholder=":", id="prompt-shell")
