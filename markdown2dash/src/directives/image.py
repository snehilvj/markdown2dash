import dash_mantine_components as dmc
from dash.development.base_component import Component

from .base import BaseDirective


class Image(BaseDirective):
    NAME = "image"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        return dmc.Image(src=title, **options)
