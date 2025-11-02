#! ./.venv/ python3

from textual.widgets import Label


class Footer(Label):
    """Footer displaying project info or placeholder."""
    
    def __init__(self, project_name: str | None):
        footer_text = f"[{project_name}]" if project_name else "\[Project Name]"
        super().__init__(footer_text, id="footer")
    