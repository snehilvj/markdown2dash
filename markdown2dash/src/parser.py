from typing import List, Optional

import mistune
from mistune.directives import RSTDirective, DirectivePlugin

from .directives.admonition import Admonition
from .directives.divider import Divider
from .directives.exec import BlockExec
from .directives.image import Image
from .directives.kwargs import Kwargs
from .directives.source import SourceCode
from .directives.toc import TableOfContents
from .renderer import DashRenderer

DEFAULT_DIRECTIVES = [
    Admonition(),
    BlockExec(),
    Divider(),
    Image(),
    Kwargs(),
    SourceCode(),
    TableOfContents(),
]


def create_parser(directives: Optional[List[DirectivePlugin]] = None):
    directives = directives or []
    directives += DEFAULT_DIRECTIVES
    return mistune.create_markdown(
        renderer=DashRenderer(),
        plugins=[
            "mark",
            "spoiler",
            "strikethrough",
            "table",
            "task_lists",
            RSTDirective(directives),
        ],
    )


parse = create_parser()
