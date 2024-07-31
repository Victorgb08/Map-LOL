import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carregar dados do arquivo JSON
with open("Data/jungler_data.json", "r") as file:
    data = json.load(file)

blue_side = data['team1']
red_side = data['team2']

# Carregar a imagem de fundo
background_image = mpimg.imread('Images/map.png')

# Função para criar e exibir o gráfico


def create_and_show_plot(side_data, color, title):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Definir a imagem de fundo
    ax.imshow(background_image, extent=[0, 15000, 0, 15000], aspect='auto')

    points = []
    for i in side_data:
        i['x'] = i['position']['x']
        i['y'] = i['position']['y']
        points.append(ax.scatter(i["x"], i["y"], color=color))
    ax.set_title(title)

    # Fixar os limites dos eixos
    ax.set_xlim(0, 15000)
    ax.set_ylim(0, 15000)

    # Função para exibir informações adicionais
    annotation = ax.annotate("", xy=(0, 0), xytext=(20, 20),
                             textcoords="offset points",
                             bbox=dict(boxstyle="round", fc="w"),
                             arrowprops=dict(arrowstyle="->"))
    annotation.set_visible(False)

    def format_info(info):
        # Renomear e filtrar as chaves
        filtered_info = {
            "Tempo (min)": info.get("timestamp"),
            "Gold total": info.get("totalGold"),
            "Farm da Jungle": info.get("jungleMinionsKilled")
        }
        formatted_text = "\n".join(
            [f"{key}: {value}" for key, value in filtered_info.items()])
        return formatted_text

    def update_annotation(event, point, info):
        annotation.xy = (event.xdata, event.ydata)
        text = format_info(info)
        annotation.set_text(text)
        annotation.set_visible(True)
        fig.canvas.draw()

    def on_click(event):
        if event.inaxes is not None:
            for i, point in enumerate(points):
                cont, _ = point.contains(event)
                if cont:
                    update_annotation(event, point, side_data[i])
                    return

    # Conectar o evento de clique
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Exibir o gráfico
    plt.show()


# Criar e exibir os gráficos
create_and_show_plot(blue_side, 'blue', 'Blue Side')
create_and_show_plot(red_side, 'red', 'Red Side')
