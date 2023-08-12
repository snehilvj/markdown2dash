import mistune
from mistune.directives import RSTDirective
from typing import Callable, Optional

from .directives.admonition import Admonition
from .directives.exec import BlockExec
from .directives.image import Image
from .directives.kwargs import Kwargs
from .directives.toc import TableOfContents
from .renderer import DashRenderer


def default_toc_renderer(self, toc):
    raise NotImplementedError


def parse(
    content: str,
    toc_renderer: Callable = default_toc_renderer,
    toc_kwargs: Optional[dict] = None,
):
    toc_kwargs = toc_kwargs or {}
    parser = mistune.create_markdown(
        renderer=DashRenderer(),
        plugins=[
            "strikethrough",
            "mark",
            "table",
            RSTDirective(
                [
                    Admonition(),
                    Image(),
                    BlockExec(),
                    Kwargs(),
                    TableOfContents(toc_renderer, **toc_kwargs),
                ]
            ),
        ],
    )
    return parser(content)
