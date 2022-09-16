import webbrowser

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import sys

csvpath = sys.argv[1]
capturedata = pd.read_csv(csvpath)
fig = px.scatter_mapbox(capturedata, lat="latitude", lon="longitude", hover_name="capture_id",
                        color_discrete_sequence=["fuchsia"], zoom=13, height=700)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 20, "t": 10, "l": 20, "b": 20})
app = dash.Dash()

app.layout = html.Div([
        html.H4('Trees detected'),
        dcc.Graph(id="graph", figure=fig),
        html.H4("Select Date of Capture"),
        dcc.RangeSlider(min=0, max=20, step=1, id="range-slider"),

])

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server(port=8050)

