from mistune.directives import DirectivePlugin
from typing import Callable, Optional

from ..utils import create_heading_id


class TableOfContents(DirectivePlugin):
    NAME = "toc"

    def __init__(
        self,
        render_func: Optional[Callable] = None,
        min_level: int = 1,
        max_level: int = 5,
    ):
        super().__init__()
        self.render_func = render_func
        self.min_level = min_level
        self.max_level = max_level

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        attrs = {
            "min_level": options.get("min_level", self.min_level),
            "max_level": options.get("max_level", self.max_level),
        }
        return {"type": "block_toc", "attrs": attrs}

    # noinspection PyMethodMayBeStatic
    def toc_hook(self, md, state):
        sections = []
        headings = []

        for tok in state.tokens:
            if tok["type"] == "block_toc":
                sections.append(tok)
            elif tok["type"] == "heading":
                headings.append(tok)

        for section in sections:
            min_level = section["attrs"].pop("min_level")
            max_level = section["attrs"].pop("max_level")

            toc = []
            for heading in headings:
                level = heading["attrs"]["level"]
                text = heading["text"]
                if int(min_level) <= int(level) <= int(max_level):
                    item = (level, text, create_heading_id(text))
                    toc.append(item)

            section["attrs"]["toc"] = toc

    # noinspection PyMethodOverriding
    def __call__(self, directive, md):
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register("block_toc", self.render_func)
            md.before_render_hooks.append(self.toc_hook)
