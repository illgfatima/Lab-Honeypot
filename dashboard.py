# dashboard.py
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

LOGFILE = "connections.csv"
df = pd.read_csv(LOGFILE) if os.path.exists(LOGFILE) else pd.DataFrame(columns=["ts","src_ip","src_port","data"])

app = Dash(__name__)
app.layout = html.Div([
    html.H3("Honeypot — Connections"),
    dcc.Graph(figure=px.bar(df.groupby("src_ip").size().reset_index(name='count'), x='src_ip', y='count', title='Top IPs')),
    html.H4("Raw logs (last 50)"),
    html.Pre(df.tail(50).to_csv(index=False))
])

if __name__ == "__main__":
    app.run_server(debug=False, host="127.0.0.1", port=8050)
