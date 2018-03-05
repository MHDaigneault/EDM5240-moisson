#coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier2 ="moisson-chaussures.csv"

url="https://www.sportsexperts.ca/fr-CA/femmes/chaussures?pagesize=451"


contenu = requests.get(url)
page = BeautifulSoup(contenu.text,"html.parser")
#print(page)

urldeschaussures = page.find_all("div", class_="product-tile-text")
# print(urldeschaussures)

chaussure = []


prix = [x.span.text for x in page.find_all('div', class_='product-tile-price')]
#print(prix)

#J'ai vraiment tenter de séparer les prix dans une colonne différente mais je n'ai pas été capable de trouver comment. Avoir le prix a vraiment été complique ( j'ai plusieurs commentaire vers lbas qui le prouve haha)

for urlchaussure in urldeschaussures:
	chaussure =[]

	try:
		url2 = urlchaussure.a["href"]
		url2 = "https://www.sportsexperts.ca" + url2
		#print(url2)

		contenu2 = requests.get(url2)
		page2 = BeautifulSoup(contenu2.text,"html.parser")
		#print(contenu2)

		brand = page2.find("span", class_="product-detail-brand").text
		#print(brand)
		chaussure.append(brand)

		categorie = page2.find("span", class_="product-detail-name").text
		#print(categorie)
		chaussure.append(categorie)


# 		# prix = page2.find(class_="product-tile-price").find_next("span").text
# 		# print(prix)s

# 		pointure = page2.find("h2", class_ = "h6").text
# 		print(pointure)
# 		# tout = page2.find("div", class_="product-detail").text
# 		# print(tout)
		
	

		f2 = open(fichier2, "a")
		xyz = csv.writer(f2)
		xyz.writerow([chaussure])


	

		
	except:
		print("rien ici")



# prix = [x.span.text for x in page.find_all('div', class_='product-tile-price')]
# print(prix)

