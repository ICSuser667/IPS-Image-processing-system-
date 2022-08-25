import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

capturedata = pd.read_csv("/home/ryan/PycharmProjects/IPS-Image-processing-system-/yolov5/runs/detect/exp/labels/_detectionids.csv")
fig = px.scatter_mapbox(capturedata, lat="latitude", lon="longitude", hover_name="capture_id",
                        color_discrete_sequence=["fuchsia"], zoom=10, height=900)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 20, "l": 0, "b": 20})
fig.show()
app = dash.Dash()

app.layout = html.Div([
    html.H4('TREES'),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)
