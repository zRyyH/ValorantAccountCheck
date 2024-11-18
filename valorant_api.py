from datetime import datetime
import requests
import traceback

headers = {
    "Authorization": 'HDEV-97da4e27-72ac-48c2-8afd-18e2d509b63b'
}

def ultima_atividade(nametag):
    try:
        if nametag:
            name, tag = nametag.split('#')
            url = f"https://api.henrikdev.xyz/valorant/v4/matches/na/pc/{name}/{tag}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data_iso = response.json()['data'][0]['metadata']['started_at']
                data_datetime = datetime.strptime(data_iso, "%Y-%m-%dT%H:%M:%S.%fZ")
                data_formatada = data_datetime.strftime("%d/%m/%Y")
                timestamp = datetime.strptime(data_formatada, "%d/%m/%Y").timestamp()
                return data_formatada
        return '????'
    except:
        traceback.print_exc()
        return '????'
    
def ultimo_rank(nametag):
    try:
        if nametag:
            name, tag = nametag.split('#')
            url = f"https://api.henrikdev.xyz/valorant/v1/mmr-history/na/{name}/{tag}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()['data'][0]
                last_rank = data['currenttierpatched']
                return last_rank
            return '????'
    except:
        traceback.print_exc()
        return '????'