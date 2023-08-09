import dash_mantine_components as dmc
from dash.development.base_component import Component
from dash_iconify import DashIconify
from mistune.directives import DirectivePlugin

from ..decorators import class_name


@class_name
def admonition(self, title, content, icon=None) -> Component:
    kwargs = {"icon": DashIconify(icon=icon, width=23)} if icon else {}
    return dmc.Alert(content, title=title, **kwargs)


class Admonition(DirectivePlugin):
    NAME = "admonition"

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        title = self.parse_title(m)
        content = self.parse_content(m)
        attrs = {"title": title, "content": content, **options}
        return {"type": "block_admonition", "attrs": attrs}

    # noinspection PyMethodOverriding
    def __call__(self, directive, md):
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register("block_admonition", admonition)
