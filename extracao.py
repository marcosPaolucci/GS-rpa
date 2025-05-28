import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL da página com os arquivos CSV diários
url = "https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/diario/Brasil/"

# Pasta local onde os arquivos serão salvos
pasta_destino = "data"
os.makedirs(pasta_destino, exist_ok=True)

# Requisição da página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Percorre os links procurando arquivos .csv
for link in soup.find_all('a', href=True):
    if link['href'].endswith('.csv'):
        arquivo_url = urljoin(url, link['href'])
        nome_arquivo = link['href'].split('/')[-1]
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

        print(f"⬇️ Baixando {arquivo_url}...")
        r = requests.get(arquivo_url)
        with open(caminho_arquivo, 'wb') as f:
            f.write(r.content)
        print(f"✅ {nome_arquivo} salvo em '{pasta_destino}/'")