import dash_mantine_components as dmc
from dash import html
from dash.development.base_component import Component

from .base import BaseDirective
from ..utils import create_heading_id


class TableOfContents(BaseDirective):
    NAME = "toc"

    # noinspection PyMethodMayBeStatic
    def hook(self, md, state):
        sections = []
        headings = []

        for tok in state.tokens:
            if tok["type"] == "block_toc":
                sections.append(tok)
            elif tok["type"] == "heading":
                headings.append(tok)

        for section in sections:
            attrs = section["attrs"]
            table_of_contents = []
            for heading in headings:
                level = heading["attrs"]["level"]
                text = heading["text"]
                item = (level, text, create_heading_id(text))
                table_of_contents.append(item)

            attrs["table_of_contents"] = table_of_contents
            attrs["title"] = attrs["title"] or "Table of Contents"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        table_of_contents = options.pop("table_of_contents")
        min_level = int(options.pop("min_level", "3"))
        paddings = {3: 0, 5: 40}
        links = [
            html.A(
                dmc.Text(text, color="indigo", size="sm"),
                href="#" + hid,
                style={
                    "textTransform": "capitalize",
                    "textDecoration": "none",
                    "paddingLeft": paddings[level],
                    "width": "fit-content",
                },
            )
            for level, text, hid in table_of_contents
            if level >= min_level
        ]
        heading = dmc.Text(title, mb=10, weight=500) if links else None
        return dmc.Stack([heading, *links], spacing=4, mt=20, mb=30, **options)
