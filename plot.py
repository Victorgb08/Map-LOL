import matplotlib.pyplot as plt
import pandas as pd
import json
import matplotlib.image as mpimg

# Carregar dados JSON a partir de um arquivo
with open('Data/jungler_data.json', 'r') as file:
    data_dict = json.load(file)

# Função para extrair dados
def extract_data(team_data):
    df = pd.DataFrame(team_data)
    df['x'] = df['position'].apply(lambda pos: pos['x'])
    df['y'] = df['position'].apply(lambda pos: pos['y'])
    df['timestamp'] = df['timestamp']
    # df['xp'] = df['xp']
    # df['jungleMinionsKilled'] = df['jungleMinionsKilled']
    # df['totalGold'] = df['totalGold']
    return df[['timestamp', 'x', 'y']]

# Carregar a imagem de fundo
background_image = mpimg.imread('Images/map.png')

# Criar DataFrames para as equipes
df_team1 = extract_data(data_dict['team1'])
df_team2 = extract_data(data_dict['team2'])

# Criar o gráfico para o Blue Side
plt.figure(figsize=(12, 8))
plt.imshow(background_image, extent=[0, 15000, 0, 15000], aspect='auto')
plt.scatter(df_team1['x'], df_team1['y'], marker='x', label='Posição', color='blue')
for i, row in df_team1.iterrows():
    plt.text(row['x'], row['y'], f"{row['timestamp']:.0f}", fontsize=10, color='yellow')

# Adicionar um ponto invisível para a legenda
plt.scatter([], [], marker='x', label='Tempo (min)', color='yellow')

plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Posição do Jungler Blue Side')
plt.xlim(0, 15000)
plt.ylim(0, 15000)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(False)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Ajustar layout para incluir a legenda
plt.savefig('Jungler Blue Side.png', bbox_inches='tight')
plt.close()

# Criar o gráfico para o Red Side
plt.figure(figsize=(12, 8))
plt.imshow(background_image, extent=[0, 15000, 0, 15000], aspect='auto')
plt.scatter(df_team2['x'], df_team2['y'], marker='x', label='Posição', color='red')
for i, row in df_team2.iterrows():
    plt.text(row['x'], row['y'], f"{row['timestamp']:.0f}", fontsize=10, color='yellow')

# Adicionar um ponto invisível para a legenda
plt.scatter([], [], marker='x', label='Tempo (min)', color='yellow')

plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Posição do Jungler Red Side')
plt.xlim(0, 15000)
plt.ylim(0, 15000)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(False)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Ajustar layout para incluir a legenda
plt.savefig('Jungler Red Side.png', bbox_inches='tight')
plt.close()
