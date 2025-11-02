#! ./.venv/ python3

from textual.widgets import Static


class WelcomeText(Static):
    """Displays the NcLabs welcome message."""
    
    def __init__(self, app_version: str, py_version: str, os_name: str):
        text = f"""
NcLabs - {app_version} [Python {py_version}] on {os_name}
For more information enter "help", "license" or "credit".

type    :help[dim]<enter>[/dim]    list of available commands
type    :q[dim]<enter>[/dim]       to exit                   

type    :changelogs[dim]<enter>[/dim] to see changes in {app_version}
"""
        super().__init__(text, id="welcome")
        