import bs4
import requests

# resultado = requests.get("https://es.wikipedia.org/wiki/Nicodemo")


# soup = bs4.BeautifulSoup(resultado.text,"lxml")
# print(soup.select('title')[0].getText())
# print(len(soup.select('p')))
# parrafo = soup.select('p')
# print(parrafo[3].getText())

# columna_lateral = soup.select(".infobox.biography.vcard")
# #print(columna_lateral)

# imagenes = soup.select('td.imagen')
# print(imagenes)

pagina_sopa = requests.get("https://www.google.com/search?sca_esv=922da51617062156&q=sopa&udm=2&fbs=AEQNm0AeMNWKf4PpcKMI-eSa16lJoRPMIuyspCxWO6iZW9F1Ns6EVsgc0W_0xN47PHaanAEtg26fpfc9gg2y1-ZsywNNidIzOA0khSyMN51n7r3LlCN1M2Qvu76xqhq8ZDzUz3QjRfF2HLyV2ldaCxuWbSUHZYxzFFv154NlyEUW1OeFwXcGcSyQr3pVDFp-PfYkJR9qH_De_cBIcEiN4tQKcLlPz-MFxQ&sa=X&ved=2ahUKEwjhubrUjPmIAxWW38kDHWmJKj0QtKgLegQIFRAB&biw=629&bih=823&dpr=2")
receta = bs4.BeautifulSoup(pagina_sopa.text,"lxml")
print(receta.select('title')[0].getText())
imagenes_sopa = receta.select("img")[3]['src']
print(imagenes_sopa)

imagen_prueba = requests.get(imagenes_sopa)

f = open('mi_imagen.jpg','wb')
f.write(imagen_prueba.content)
f.close()
