import dash_mantine_components as dmc
from dash import Dash

from markdown2dash import create_parser
from scroll import ScrollToTop

with open("../README.md") as f:
    md = f.read()

parse = create_parser([ScrollToTop()])
layout = parse(md)

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = Dash(__name__, external_stylesheets=stylesheets)
server = app.server

app.layout = dmc.MantineProvider(
    dmc.Container(layout, size="lg", p=20),
    id="m2d-mantine-provider",
    forceColorScheme="light",
    theme={
        "primaryColor": "indigo",
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Table": {
                "defaultProps": {
                    "striped": True,
                    "withTableBorder": True,
                    "highlightOnHover": True,
                }
            },
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
        },
    },
)

if __name__ == "__main__":
    app.run()
