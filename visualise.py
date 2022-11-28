import webbrowser

import dash
from dash import dcc
from dash import html, Input, Output
import plotly.express as px
import pandas as pd
import sys

csvpath = sys.argv[1]
capturedata = pd.read_csv(csvpath)
numdate = [x for x in (capturedata['capture_date'].unique())]
d1 = dict(enumerate(numdate))
print(d1)
fig = px.scatter_mapbox(capturedata, lat='latitude', lon='longitude',
                            hover_name="capture_id",
                            color_discrete_sequence=["fuchsia"], zoom=13, height=700)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 20, "t": 10, "l": 20, "b": 20})
app = dash.Dash()

app.layout = html.Div([
    html.H4('Trees detected'),
    dcc.Graph(id="graph", figure=fig),
    html.H4("Select Date of Capture"),
    dcc.Slider(min(d1.keys()), (max(d1.keys())), step=None,
               marks={i: d1[i] for i in d1}, id="range-slider")

])


@app.callback(
    Output("graph", "figure"),
    Input("range-slider", "value"),
)
def update_graph(selected_capture_date):
    print(selected_capture_date)
    filtered_data = capturedata[capturedata.capture_date == d1[selected_capture_date]]

    fig = px.scatter_mapbox(filtered_data, lat='latitude', lon='longitude',
                            hover_name="capture_id",
                            color_discrete_sequence=["fuchsia"], zoom=13, height=700)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 20, "t": 10, "l": 20, "b": 20})
    return fig


if __name__ == '__main__':
    webbrowser.open_new("127.0.0.1:8050")
    app.run_server(port=8050)
