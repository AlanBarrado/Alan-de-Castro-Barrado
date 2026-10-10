import requests as r
from bs4 import BeautifulSoup

print("-Aula de Scraping/Crawling-")

try:
    resultado = r.get("https://uol.com.br/start/esport")
except:
    print("Erro: não foi possivel acessar a página")
else:
    resposta = resultado.text
    soup = BeautifulSoup(resposta, 'html.parser')

    print(soup.title.string)

    lista = ["Neymar", "CSGO", "free fire", "pokemon", "cod"]
    for paragrafo in soup.find_all('body'):
        for palavra in lista:
            for paragrafo_str in paragrafo.stripped_strings:
                if palavra.upper() in str(paragrafo_str).upper():
                    print(f"noticia encontrada: {paragrafo_str}")