from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://informacoes.anatel.gov.br/legislacao/index.php/component/content/article?id=1205")
bs = BeautifulSoup(html, 'html.parser')


linhas = bs.find_all('span', {'class':'documentModified'})



## Imprime todo texto contido em cada linha ##
for i in linhas:
    print(i.text)

#print(bs.prettify())