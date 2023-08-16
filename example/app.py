import dash_mantine_components as dmc
from dash import Dash

from markdown2dash import parse

with open("../README.md") as f:
    md = f.read()

layout = parse(md)

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
