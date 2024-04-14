import dash_mantine_components as dmc
from dash.development.base_component import Component

from .base import BaseDirective


class Divider(BaseDirective):
    NAME = "divider"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        return dmc.Divider(label=title, **options)
