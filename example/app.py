import dash_mantine_components as dmc
from dash import Dash, html

from markdown2dash import parse

with open("../README.md") as f:
    md = f.read()


def render_toc(self, toc):
    paddings = {3: 0, 5: 40}
    links = [
        html.A(
            dmc.Text(text, color="indigo", size="sm"),
            href="#" + hid,
            style={
                "textTransform": "capitalize",
                "textDecoration": "none",
                "paddingLeft": paddings[level],
                "width": "fit-content",
            },
        )
        for level, text, hid in toc
    ]
    heading = dmc.Text("Table of Contents", mb=10, weight=500) if links else None
    return dmc.Stack([heading, *links], spacing=4, mt=20, mb=30)


layout = parse(md, toc_renderer=render_toc)

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    dmc.Container(layout, size="lg", p=20),
    withGlobalStyles=True,
    withNormalizeCSS=True,
    theme={
        "primaryColor": "indigo",
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Table": {"defaultProps": {"striped": True, "withBorder": True}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
        },
    },
)

if __name__ == "__main__":
    app.run(debug=True)
