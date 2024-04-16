import dash_mantine_components as dmc

data = [
    {
        "month": "January",
        "Smartphones": 1200,
        "Laptops": 900,
        "Tablets": 200,
        "Watches": 700,
    },
    {
        "month": "February",
        "Smartphones": 1900,
        "Laptops": 1200,
        "Tablets": 400,
        "Watches": 200,
    },
    {
        "month": "March",
        "Smartphones": 400,
        "Laptops": 1000,
        "Tablets": 200,
        "Watches": 400,
    },
    {
        "month": "April",
        "Smartphones": 1000,
        "Laptops": 200,
        "Tablets": 800,
        "Watches": 900,
    },
    {
        "month": "May",
        "Smartphones": 800,
        "Laptops": 1400,
        "Tablets": 1200,
        "Watches": 1000,
    },
    {
        "month": "June",
        "Smartphones": 750,
        "Laptops": 600,
        "Tablets": 1000,
        "Watches": 100,
    },
]

component = dmc.BarChart(
    h=300,
    data=data,
    dataKey="month",
    series=[
        {"name": "Smartphones", "color": "violet.6"},
        {"name": "Laptops", "color": "blue.6"},
        {"name": "Tablets", "color": "teal.6"},
        {"name": "Watches", "color": "indigo.6"},
    ],
    tickLine="y",
)
