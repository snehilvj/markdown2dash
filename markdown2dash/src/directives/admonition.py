import dash_mantine_components as dmc
from dash_iconify import DashIconify

from .base import BaseDirective


class Admonition(BaseDirective):
    NAME = "admonition"

    def render(self, renderer, title: str, content: str, **options):
        icon = options.get("icon")
        if icon:
            options["icon"] = DashIconify(icon=icon, width=23)
        return dmc.Alert(content, title=title, **options)
