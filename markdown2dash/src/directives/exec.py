import importlib
import inspect

import dash_mantine_components as dmc
from dash.development.base_component import Component

from .base import BaseDirective


class BlockExec(BaseDirective):
    NAME = "exec"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        code = options.pop("code", "true")
        border = options.pop("border", "true")
        imported = importlib.import_module(title)
        components = [
            dmc.Paper(
                getattr(imported, "component"), withBorder=border == "true", p="xl"
            )
        ]
        if code == "true":
            source = inspect.getsource(imported).replace("component = ", "", 1)
            prism = dmc.Prism(source, language="python")
            components.append(prism)
        return dmc.Box(components, **options)
