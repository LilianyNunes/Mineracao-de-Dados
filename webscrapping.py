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

    # Encontrando os nomes dos smartphones
    produtos = soup.find_all("h2", class_="ProductCard_ProductCard_Name__U_mUQ")

    # Encontrando os preços dos smartphones
    precos = soup.find_all("p", class_="Text_Text__ARJdp Text_MobileHeadingS__HEz7L")

    # Criando listas para armazenar os dados
    lista_produtos = [produto.get_text(strip=True) for produto in produtos[:5]]
    lista_precos = [preco.get_text(strip=True) for preco in precos[:5]]

    # Exibindo os resultados no terminal
    print("📌 Lista de Smartphones e Preços:")
    for i in range(len(lista_produtos)):
        print(f"{i+1}. {lista_produtos[i]} - {lista_precos[i]}")

else:
    print(f"❌ Erro ao acessar o site. Código HTTP: {response.status_code}")
