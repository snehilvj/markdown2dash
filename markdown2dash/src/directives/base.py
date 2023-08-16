from dash.development.base_component import Component
from mistune.directives import DirectivePlugin

from ..decorators import class_name


class BaseDirective(DirectivePlugin):
    NAME = "base"

    def __init__(self):
        super().__init__()
        self.block_name = "block_" + self.NAME

    def render(self, renderer, title: str, content: str, **options) -> Component:
        raise NotImplementedError

    # noinspection PyMethodMayBeStatic
    def hook(self, md, state):
        pass

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        title = self.parse_title(m)
        content = self.parse_content(m)
        attrs = {"title": title, "content": content, **options}
        return {"type": self.block_name, "attrs": attrs}

    # noinspection PyMethodOverriding
    def __call__(self, directive, md):
        renderer = class_name(self.render)
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register(self.block_name, renderer)
            md.before_render_hooks.append(self.hook)
