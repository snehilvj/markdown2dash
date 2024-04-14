import dash_mantine_components as dmc
from dash import clientside_callback, Output, Input
from dash_iconify import DashIconify

component = dmc.Affix(
    dmc.Switch(
        onLabel=DashIconify(icon="radix-icons:moon", width=15),
        offLabel=DashIconify(icon="radix-icons:sun", width=15),
        id="theme-switch",
        checked=False,
        size="lg",
        radius="sm"
    ),
    position={"top": 20, "right": 20},
)

clientside_callback(
    """
    function(checked) {
        return checked ? "dark" : "light"
    }
    """,
    Output("m2d-mantine-provider", "forceColorScheme"),
    Input("theme-switch", "checked"),
    prevent_initial_call=True,
)
