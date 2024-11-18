import requests
import traceback
from valorant_api import ultima_atividade, ultimo_rank


# URL para a requisição
url = "https://api.awpsoft.com.br/api/"


def getAccounts():
    try:
        # Fazer a requisição GET
        response = requests.get(url+'accounts')

        # Verificar o status da resposta
        if response.status_code == 200:
            accounts = response.json()  # Se o retorno for JSON

            if accounts:
                return accounts
        else:
            print("Erro ao fazer a requisição. Código:", response.status_code)
    
    except:
        traceback.print_exc()


def postAccount(**kwargs):
    try:
        print(kwargs)
        payload = {}
        payload.update(kwargs)


        # Fazer a requisição GET
        response = requests.put(url+'account', json=payload)
        print(response)

        if response:
            pass
        else:
            print("Erro ao fazer a requisição. Código:", response.status_code)

    except:
        traceback.print_exc()



accounts = getAccounts()

for account in accounts['mensagem']:
    try:
        nametag = account['nametag']

        account['ultimaAtividade'] = ultima_atividade(nametag)
        account['elo'] = ultimo_rank(nametag)

        account.pop('dataRegistro')

        postAccount(**account)
    
    except:
        traceback.print_exc()