import requests
import datetime

def gravar_em_arquivo(valor):
    data = datetime.date.today()
    with open('cotacao_log.txt', 'a') as file:
        file.write(f'{data.strftime("%d/%m/%Y")} - {valor}\n')

def main(moeda):
    r = requests.get(f'https://economia.awesomeapi.com.br/all/{moeda}-BRL')
    if r.status_code == 200:
        valor = r.json()[f'{moeda}']['low']
    else:
        valor = f'-Erro: {r.status_code}'
      
    return str(valor)

