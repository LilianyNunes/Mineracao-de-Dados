import requests
from bs4 import BeautifulSoup

# Definição do User-Agent para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# URL do site com lista de smartphones
url = "https://www.buscape.com.br/celular"

# Fazendo a requisição HTTP
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("Página acessada com sucesso!")
else:
    print(f"Erro ao acessar o site. Código HTTP: {response.status_code}")
