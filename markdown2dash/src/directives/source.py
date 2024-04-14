import dash_mantine_components as dmc
from dash.development.base_component import Component

from .base import BaseDirective


class SourceCode(BaseDirective):
    NAME = "source"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        language = options.pop("language", "python")
        with open(title, "r") as f:
            source = f.read()
        return dmc.CodeHighlight(source, language=language)
