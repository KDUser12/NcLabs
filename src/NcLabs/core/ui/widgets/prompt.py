#! ./.venv/ python3

from textual.widgets import Input


class PromptInput(Input):
    """Input field acting as NcLabs command prompt."""
    
    def __init__(self):
        super().__init__(placeholder=":", id="prompt-shell")
