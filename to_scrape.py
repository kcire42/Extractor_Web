import bs4
import requests
from word2number import w2n
import pandas as pd 

titulos = []
calificacion = []
for page in range(1,51):
    link = "https://books.toscrape.com/catalogue/page-{}.html".format(page)
    pagina_to_scrape = requests.get(link)
    #print(pagina_to_scrape)
    toscrape = bs4.BeautifulSoup(pagina_to_scrape.text,"lxml")
    #print(toscrape.select("title")[0].getText())
    articulos = toscrape.select("li.col-xs-6.col-sm-4.col-md-3.col-lg-3")
    for articulo in articulos:
        get_titulo = articulo.select_one('h3 a')
        get_stars = articulo.select_one('p')
        titulo = get_titulo['title']
        stars = get_stars['class'][1]
        if w2n.word_to_num(stars) > 3:
            titulos.append(titulo)
            calificacion.append(stars)

df = pd.DataFrame({'Titulos':titulos,'Estrellas':calificacion})
print(df)
            



# Iterar sobre todas las etiquetas <p> encontradas e imprimir su contenido


