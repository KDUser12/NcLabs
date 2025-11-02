#! ./.venv/ python3

from textual.app import App
import platform
import sys
from textual.screen import Screen

from .screens.main_screen import MainScreen


class NcLabsApp(App):
    """NcLabs Textual interface entry point."""
    
    CSS_PATH = "styles/base.tcss"
    
    BINDINGS = [
        ("q", "quit", "Quit"),
        (":", "focus_prompt", "Focus prompt")
    ]
    
    def __init__(self):
        super().__init__()
        self.version = self._get_version()
        self.os = platform.system()
        self.environment_version = ".".join(map(str, sys.version_info[:3]))
        self.project_name = None
        
        
    def _get_version(self) -> str:
        """_get_version Retrieve the current NcLabs version.

        This method attempts to import the `__version__` attribute from the
        main NcLabs package. If the import fails (for example, when the
        version file is missing or the package is not fully initialized),
        it safely returns a fallback version of "0.0.0" instead of raising
        an exception.

        Returns:
            str -- The current NcLabs version string (e.g., "1.2.0"), or "0.0.0" if unavailable.
        """
        
        try:
            from __init__ import __version__
            return __version__
        except Exception:
            return "0.0.0"
        
        
    def on_mount(self):
        """Mount the main screen."""
        self.theme = "flexoki"
        self.push_screen(MainScreen(self))
        
    
    def action_focus_prompt(self):
        screen: Screen = self.screen
        prompt = screen.query_one("#prompt-shell")
        prompt.focus()
        