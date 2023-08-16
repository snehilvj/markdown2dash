import importlib
import inspect

import dash_mantine_components as dmc
from dash import html
from dash.development.base_component import Component

from .base import BaseDirective
from ..utils import convert_docstring_to_dict


class Kwargs(BaseDirective):
    NAME = "kwargs"

    # noinspection PyMethodMayBeStatic
    def hook(self, md, state):
        sections = []

        for tok in state.tokens:
            if tok["type"] == self.block_name:
                sections.append(tok)

        for section in sections:
            attrs = section["attrs"]
            package = attrs.pop("library", "dash_mantine_components")
            component_name = attrs["title"]
            imported = importlib.import_module(package)
            component = getattr(imported, component_name)
            docstring = inspect.getdoc(component).split("Keyword arguments:")[-1]
            attrs["kwargs"] = convert_docstring_to_dict(docstring)

    def render(self, renderer, title: str, content: str, **options) -> Component:
        data = options.pop("kwargs")
        head = renderer.table_head(
            [renderer.table_cell(col.title(), head=True) for col in data[0]]
        )
        body = renderer.table_body(
            [
                renderer.table_row([renderer.table_cell(col) for col in row.values()])
                for row in data
            ]
        )
        table = dmc.Table([head, body], **options)
        return table
