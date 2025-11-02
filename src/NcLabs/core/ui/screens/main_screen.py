#! ./.venv/ python3

from textual.screen import Screen
from textual.containers import Container

from ..widgets.welcome import WelcomeText
from ..widgets.footer import Footer
from ..widgets.prompt import PromptInput


class MainScreen(Screen):
    """Main interactive NcLabs screen."""
    
    def __init__(self, app_ref):
        super().__init__()
        self.app_ref = app_ref
        
    
    def compose(self):
        yield Container(
            WelcomeText(
                app_version=self.app_ref.version,
                py_version=self.app_ref.environment_version,
                os_name=self.app_ref.os
            ),
            id="welcome-container"
        )
        yield Footer(project_name=self.app_ref.project_name)
        yield PromptInput()
        