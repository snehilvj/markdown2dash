import importlib
import inspect

import dash_mantine_components as dmc
from dash.development.base_component import Component
from mistune.directives import DirectivePlugin

from ..decorators import class_name


@class_name
def kwargs(self, component: str, library: str) -> Component:
    lib = importlib.import_module(library)
    clazz = getattr(lib, component)
    docs = inspect.getdoc(clazz)
    docs = docs.split("Keyword arguments:")[-1]
    return dmc.Prism(docs, language="git", noCopy=True)


class Kwargs(DirectivePlugin):
    NAME = "kwargs"

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        component = self.parse_title(m)
        # content = self.parse_content(m)
        attrs = {
            "component": component,
            "library": options.get("library", "dash_mantine_components"),
        }
        return {"type": "block_kwargs", "attrs": attrs}

    # noinspection PyMethodOverriding
    def __call__(self, directive, md):
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register("block_kwargs", kwargs)
