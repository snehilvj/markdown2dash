from typing import List, Optional

import mistune
from mistune.directives import RSTDirective, DirectivePlugin

from .directives.admonition import Admonition
from .directives.exec import BlockExec
from .directives.image import Image
from .directives.kwargs import Kwargs
from .directives.toc import TableOfContents
from .renderer import DashRenderer

DEFAULT_DIRECTIVES = [Admonition(), Image(), BlockExec(), Kwargs(), TableOfContents()]


def parse(content: str, directives: Optional[List[DirectivePlugin]] = None):
    directives = directives or DEFAULT_DIRECTIVES
    parser = mistune.create_markdown(
        renderer=DashRenderer(),
        plugins=[
            "strikethrough",
            "mark",
            "table",
            RSTDirective(directives),
        ],
    )
    return parser(content)
