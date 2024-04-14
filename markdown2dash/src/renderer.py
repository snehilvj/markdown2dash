from urllib.parse import urlparse

import dash_mantine_components as dmc
from dash.development.base_component import Component
from mistune import safe_entity, HTMLRenderer

from .decorators import class_name
from .utils import create_heading_id


def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result


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

    @class_name
    def emphasis(self, text: str) -> Component:
        return dmc.Text(text, fs="italic", display="inline")

    @class_name
    def strong(self, text: str) -> Component:
        return dmc.Text(text, fw="bold", display="inline")

    @class_name
    def codespan(self, text: str) -> Component:
        return dmc.Code(text)

    @class_name
    def heading(self, text: str, level: int, **attrs) -> Component:
        return dmc.Title(text, order=level, id=create_heading_id(text[0]))

    @class_name
    def thematic_break(self) -> Component:
        return dmc.Divider()

    def block_text(self, text: str) -> str:
        return text

    @class_name
    def block_code(self, code: str, info=None) -> Component:
        if info is not None:
            info = safe_entity(info.strip())
        if info:
            lang = info.split(None, 1)[0]
            return dmc.CodeHighlight(code, language=lang)
        else:
            return dmc.Code(code)

    @class_name
    def block_quote(self, text: str) -> Component:
        return dmc.Blockquote(text)

    @class_name
    def list_item(self, text: list) -> Component:
        text = flatten(text)
        return dmc.ListItem(text)

    @class_name
    def list(self, text, ordered: bool, **attrs) -> Component:
        return dmc.List(
            text, type="ordered" if ordered else "unordered", withPadding=True
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
        return dmc.TableThead(self.table_row(text))

    @class_name
    def table_body(self, text: Component) -> Component:
        return dmc.TableTbody(text)

    @class_name
    def table_row(self, text: str) -> Component:
        return dmc.TableTr(text)

    @class_name
    def table_cell(self, text: str, align=None, head=False) -> Component:
        return dmc.TableTh(text) if head else dmc.TableTd(text)

    def blank_line(self) -> None:
        return

    @class_name
    def block_spoiler(self, children: Component) -> Component:
        return dmc.Spoiler(children, hideLabel="Show less", showLabel="Show more")

    @class_name
    def task_list_item(self, text: list, checked: bool, **attrs):
        text = flatten(text)
        return dmc.ListItem(
            dmc.Checkbox(dmc.Text(text), checked=checked),
            style={"listStyleType": "none"},
        )

    def render_tokens(self, tokens, state):
        return list(self.iter_tokens(tokens, state))
