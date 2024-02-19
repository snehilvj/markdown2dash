from typing import List
from urllib.parse import urlparse

import dash_mantine_components as dmc
from dash import html
from dash.development.base_component import Component
from mistune import safe_entity, HTMLRenderer

from .decorators import class_name
from .utils import create_heading_id

# -- For image shape decoding
import cv2
import numpy as np
from urllib.request import urlopen
from dash import get_app

# noinspection PyMethodMayBeStatic
class DashRenderer(HTMLRenderer):
    NAME = "dash"

    def text(self, text: str) -> str:
        return text

    @class_name
    def link(self, text: str, url: str, title=None) -> Component:
        return dmc.Anchor(
            text,
            href=url,
            target="_blank" if bool(urlparse(url).netloc) else "_self",
            underline=False,
        )

    @class_name
    def paragraph(self, text: str) -> Component:
        return dmc.Text(text)

    # -- softbreak is not overridden. Mistune 3.0.2 returns '\n'

    @class_name
    def emphasis(self, text: str) -> Component:
        return dmc.Text(text, fs="italic", style={"display":"inline"})

    @class_name
    def strong(self, text: str) -> Component:
        return dmc.Text(text, weight="bold" , style={"display":"inline"})

    @class_name
    def codespan(self, text: str) -> Component:
        return dmc.Code(text)

    @class_name
    def heading(self, text: str, level: int, **attrs) -> Component:
        return dmc.Title(text, order=level, id=create_heading_id(text[0]))

    @class_name
    def thematic_break(self) -> Component:
        return dmc.Divider()

    @class_name
    def image(self, text: str, url: str, title=None):
        def get_image_width(url, readFlag=cv2.IMREAD_COLOR, default=200):
            # https://stackoverflow.com/questions/21061814/how-can-i-read-an-image-from-an-internet-url-in-python-cv2-scikit-image-and-mah
            if url[0] == "/":   # A relative URL
                try:
                    flaskroot = get_app().server.root_path
                    filepath = flaskroot + url
                    image = cv2.imread(filepath) 
                    return image.shape[1]
                except:
                    return default
            else:               # Assume an actual url
                try:
                    resp = urlopen(url)
                    npimage = np.asarray(bytearray(resp.read()), dtype="uint8")
                    image = cv2.imdecode(npimage, readFlag)
                    return image.shape[1]
                except:
                    return default

        # This approach to setting the width and margin allows it to be overriden in CSS by: 
        # .m2d-image .mantine-Image-imageWrapper {width: ...} etc.
        # ...then all images in a markdown file will come out the same width
        # It should be possible to set different widths for different markdown files by wrapping the 
        # output of markdown2dash.parse with classed containers and restricting this width formatting to those classes
        width = get_image_width(url)

        result = dmc.Image(
            src=url, 
            alt=text[0], 
            caption=title, 
            styles={
                "imageWrapper":{
                    "width":width,
                },
            }
        )
        return result

    def block_text(self, text: str) -> str:
        return text

    @class_name
    def block_code(self, code: str, info=None) -> Component:
        if info is not None:
            info = safe_entity(info.strip())
        if info:
            lang = info.split(None, 1)[0]
            return dmc.Prism(code, language=lang)
        else:
            return dmc.Code(code)

    @class_name
    def block_quote(self, text: str) -> Component:
        return dmc.Blockquote(text)

    @class_name
    def list_item(self, text: str) -> Component:
        if isinstance(text, list):
            text2 = []
            for item in text:
                if isinstance(item, list):
                    text2.extend(item)
                else:
                    text2.append(item)
            return dmc.ListItem(text2)
        else:
            return dmc.ListItem(text)

    @class_name
    def list(self, text: List[dmc.ListItem], ordered: bool, **attrs) -> Component:
        return dmc.List(
            text,
            type="ordered" if ordered else "unordered",
            withPadding=True,
        )

    @class_name
    def strikethrough(self, text: str) -> Component:
        return dmc.Text(text, td="line-through")

    @class_name
    def mark(self, text: str) -> Component:
        return dmc.Mark(text)

    @class_name
    def table(self, text: Component) -> Component:
        return dmc.Table(text)

    @class_name
    def table_head(self, text: str) -> Component:
        return html.Thead(html.Tr(text))

    @class_name
    def table_body(self, text: Component) -> Component:
        return html.Tbody(text)

    @class_name
    def table_row(self, text: str) -> Component:
        return html.Tr(text)

    @class_name
    def table_cell(self, text: str, align=None, head=False):
        return html.Th(text) if head else html.Td(text)

    def blank_line(self) -> None:
        return

    def render_tokens(self, tokens, state):
        components = list(self.iter_tokens(tokens, state))
        return [comp for comp in components if comp is not None]

    # -- Display alerts for unimplemented functions

    def _m2d_notimplemented(self, text):
        return dmc.Alert(f"Not implemented in dash2markdown: {text}", 
                         title="Not Implemented")
    
    def linebreak(self):
        return self._m2d_notimplemented("linebreak")
    
    def inline_html(self, html: str):
        return self._m2d_notimplemented("inline_html")
    
    def block_html(self, html: str):
        return self._m2d_notimplemented("block_html")
    
    def block_error(self, text: str):
        return self._m2d_notimplemented("block_error")

    # -- ..._math methods here are never called, since "math" is not included as a plugin in parser.py
    def block_math(self, text):
        return self._m2d_notimplemented("block_math")

    def inline_math(self, text):
        return self._m2d_notimplemented("inline_math")
