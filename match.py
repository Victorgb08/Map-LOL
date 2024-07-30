from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

region='americas'

headers = {
    'X-Riot-Token': os.getenv('API_KEY')
}

def get_match_timeline(match_id, headers):
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        return response
    else:
        print('Error:', response.status_code)
        print(response.json())

match_timeline = get_match_timeline('BR1_2976813059', headers)

with open('Data/timeline.json', 'w') as file:
    json.dump(match_timeline, file, indent=4)