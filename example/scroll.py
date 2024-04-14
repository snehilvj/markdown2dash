import uuid

import dash_mantine_components as dmc
from dash import html, Output, Input, clientside_callback, MATCH
from dash.development.base_component import Component
from dash_iconify import DashIconify

from markdown2dash import BaseDirective, create_parser


class ScrollToTop(BaseDirective):
    NAME = "scroll"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        comp_id = str(uuid.uuid4())
        clientside_callback(
            """
            function(n_clicks) {
                window.scrollTo(0, 0, "smooth")
                return null
            }
            """,
            Output({"type": "empty-container", "index": MATCH}, "children"),
            Input({"type": "scroll-button", "index": MATCH}, "n_clicks"),
            prevent_initial_call=True,
        )
        component = dmc.Affix(
            [
                html.Div(id={"type": "empty-container", "index": comp_id}),
                dmc.Button(
                    "Scroll to top",
                    id={"type": "scroll-button", "index": comp_id},
                    rightSection=DashIconify(icon="radix-icons:arrow-up"),
                    fw=400,
                ),
            ],
            position={"bottom": 20, "right": 20},
        )
        return component


parser = create_parser([ScrollToTop()])
