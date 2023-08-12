import importlib
import inspect

import dash_mantine_components as dmc
from dash.development.base_component import Component
from mistune.directives import DirectivePlugin

from ..decorators import class_name


@class_name
def block_exec(self, module: str, code: str, border: str) -> Component:
    imported = importlib.import_module(module)
    components = [
        dmc.Paper(getattr(imported, "component"), withBorder=border == "true", p="xl")
    ]
    if code == "true":
        source = inspect.getsource(imported).replace("component = ", "", 1)
        prism = dmc.Prism(source, language="python")
        components.append(prism)
    return dmc.Box(components)


class BlockExec(DirectivePlugin):
    NAME = "exec"

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        module = self.parse_title(m)
        # content = self.parse_content(m)
        attrs = {
            "module": module,
            "code": options.get("code", "true"),
            "border": options.get("border", "true"),
        }
        return {"type": "block_exec", "attrs": attrs}

    # noinspection PyMethodOverriding
    def __call__(self, directive, md):
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register("block_exec", block_exec)
