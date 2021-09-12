"""


"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

search = input('Digite o que voĉe quer pesquisar\n--> ')
storage = []
response = requests.get(f"https://lista.mercadolivre.com.br/{search}")

site = response.content  # tentar alterar depois para .text
beauty_site = BeautifulSoup(site, 'html.parser')

collecting_data = beauty_site.findAll(
    'a', attrs={'class': 'ui-search-result__content ui-search-link'})

for products in collecting_data:
    price = products.find('span', attrs={'class': 'price-tag-fraction'}).text
    link = products['href']
    product = products.find('h2', attrs={
                            'class': 'ui-search-item__title ui-search-item__group__element'}).text
    cent = products.find('span', attrs={'class': 'price-tag-cent'})
    separator = products.find(
        'span', attrs={'class': 'price-tag-decimal-separator'})
    if separator:
        value = (f'{price}{separator.text}00',)
        storage.append([product, value, link])
    elif cent:
        value = (f'{price},{cent}',)
        storage.append([product, value, link])
    else:
        storage.append([product, price, link])

data_fm = pd.DataFrame(storage, columns=['Produto', 'Preço', 'Link'])


data_fm.to_csv('produtos.csv', index=False)
