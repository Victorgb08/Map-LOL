import json
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import os

with open("Data/jungler_data.json", "r") as file:
    data = json.load(file)

blue_side = data['team1']
red_side = data['team2']

background_image = Image.open('Images/map.png')


def create_and_show_plot(side_data, color, title):
    fig = go.Figure()

    fig.add_layout_image(
        dict(
            source=background_image,
            xref="x",
            yref="y",
            x=0,
            y=15000,
            sizex=15000,
            sizey=15000,
            sizing="stretch",
            opacity=1,
            layer="below"
        )
    )

    for i in side_data:
        i['x'] = i['position']['x']
        i['y'] = i['position']['y']
        fig.add_trace(go.Scatter(
            x=[i["x"]],
            y=[i["y"]],
            mode='markers',
            marker=dict(color=color),
            text=f"Tempo (min): {i['timestamp']}<br>Gold total: {
                i['totalGold']}<br>Farm da Jungle: {i['jungleMinionsKilled']}",
            hoverinfo='text'
        ))

    fig.update_xaxes(range=[0, 15000], showgrid=False)
    fig.update_yaxes(range=[0, 15000], scaleanchor="x",
                     scaleratio=1, showgrid=False)

    fig.update_layout(
        title=title,
        xaxis_title="X",
        yaxis_title="Y",
        width=600,
        height=600,
        showlegend=False
    )

    fig.show()

    output_dir = "Maps"
    os.makedirs(output_dir, exist_ok=True)
    fig.write_html(os.path.join(output_dir, f"{title}.html"))


# Criar e exibir os gráficos
create_and_show_plot(blue_side, 'blue', 'Blue Side')
create_and_show_plot(red_side, 'red', 'Red Side')
