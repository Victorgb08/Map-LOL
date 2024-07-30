import json

# Carregar o arquivo JSON
with open('Data/timeline.json', 'r') as file:
    data = json.load(file)

# Função para identificar os junglers
def identify_junglers(data):
    jungle_minions_killed = {}

    # Inicializar dicionário para contar os minions da selva mortos por participante
    for participant_id in range(1, 11):
        jungle_minions_killed[participant_id] = 0

    # Percorrer os frames para contar os minions da selva mortos
    for frame in data['info']['frames']:
        for participant_id, participant_data in frame['participantFrames'].items():
            jungle_minions_killed[participant_data['participantId']] += participant_data.get('jungleMinionsKilled', 0)

    # Separar os participantes por time
    team1 = {k: v for k, v in jungle_minions_killed.items() if k <= 5}
    team2 = {k: v for k, v in jungle_minions_killed.items() if k > 5}

    # Identificar os junglers com base no maior número de minions da selva mortos
    jungler_team1 = max(team1, key=team1.get)
    jungler_team2 = max(team2, key=team2.get)

    return jungler_team1, jungler_team2

# Identificar os junglers
jungler_team1, jungler_team2 = identify_junglers(data)

# Função para extrair posições dos junglers ao longo do tempo
def extract_positions(data, jungler_team1, jungler_team2):
    positions = {
        'team1': [],
        'team2': []
    }

    # Percorrer os frames e coletar as posições dos junglers
    for frame in data['info']['frames']:
        timestamp = round(frame['timestamp'] / 60000,0)  # Convertendo de milissegundos para minutos
        participant_frames = frame['participantFrames']

        if str(jungler_team1) in participant_frames:
            position = participant_frames[str(jungler_team1)].get('position')
            totalGold = participant_frames[str(jungler_team1)].get('totalGold')
            xp = participant_frames[str(jungler_team1)].get('xp')
            jungleMinionsKilled = participant_frames[str(jungler_team1)].get('jungleMinionsKilled')
            if position:
                positions['team1'].append({'timestamp': timestamp, 'position': position, 'totalGold': totalGold, 'xp': xp, 'jungleMinionsKilled': jungleMinionsKilled})

        if str(jungler_team2) in participant_frames:
            position = participant_frames[str(jungler_team2)].get('position')
            totalGold = participant_frames[str(jungler_team2)].get('totalGold')
            xp = participant_frames[str(jungler_team2)].get('xp')
            jungleMinionsKilled = participant_frames[str(jungler_team2)].get('jungleMinionsKilled')
            if position:
                positions['team2'].append({'timestamp': timestamp, 'position': position, 'totalGold': totalGold, 'xp': xp, 'jungleMinionsKilled': jungleMinionsKilled})

    return positions

# Extrair posições dos junglers
positions = extract_positions(data, jungler_team1, jungler_team2)

# Opcional: Salvar as informações extraídas em um arquivo JSON
with open('Data/jungler_data.json', 'w') as file:
    json.dump(positions, file, indent=4)
