import dash_mantine_components as dmc
from dash.development.base_component import Component
from mistune.directives.image import Image as MistuneImage

from ..decorators import class_name


@class_name
def image(self, src: str, alt=None, width=None, height=None, **attrs) -> Component:
    return dmc.Image(src=src, alt=alt, width=width, height=height, **attrs)


class Image(MistuneImage):
    def __call__(self, directive, md):
        directive.register(self.NAME, self.parse)
        if md.renderer.NAME == "dash":
            md.renderer.register("block_image", image)
