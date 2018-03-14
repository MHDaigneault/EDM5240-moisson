#coding: utf-8

### BONJOUR, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses ###

### Tout d'abord, il manquait juste un «.py» à la fin de ton script...

import csv
import requests
from bs4 import BeautifulSoup

fichier2 ="moisson-chaussures.csv"

# url="https://www.sportsexperts.ca/fr-CA/femmes/chaussures?pagesize=451"

### Le dernier paramètre dans l'URL donne le nombre d'items affiché dans la page.
### Je sais que quand on clique sur «Tous», ça n'affiche que 451 des 501 items
### Mais j'ai essayé de mettre 501 à la place, et ça marche. Il y a 501 items dans la page
url="https://www.sportsexperts.ca/fr-CA/femmes/chaussures?pagesize=501"

### En regardant ce que tu as tenté de moissonner, je me suis dit:
### Défi: pourquoi s'arrêter aux chaussures pour femmes et ne pas tenter de moissonner tout le site
### Ici, je me crée un dictionnaire qui contient toutes les sections et sous-sections du site

menu = {
	"femmes":["vetements","chaussures","accessoires","nouveautes"],
	"hommes":["vetements","chaussures","accessoires","nouveautes"],
	"enfants":["accessoires","garcons","filles","nouveautes"],
	"accessoires":["sacs","technologies-dentrainement-electronique","lunettes-soleil","lunettes-de-sports-dhiver","gants-mitaines","foulards","tuques"],
	"sports":["basketball","hockey","baseball","badminton","football","golf","natation","soccer","tennis","tennis-de-table","course-a-pied","course-sur-sentier","loisirs","mise-en-forme","ski-alpin","ski-de-fond","ski-de-randonnee-alpine","volleyball","yoga","planche-à-neige","raquette-a-neige"],
	"plein-air":["hommes","femmes","equipements","nouveautes"]
}

### Pour le kik, je me définis un compteur
n = 0

### La boucle ci-dessous crée les URLs de toutes les sous-sections du site
for niv1 in menu.keys():
	# print(niv1)
	for niv2 in menu[niv1]:
		# print(niv2)
		url = "https://www.sportsexperts.ca/fr-CA/{}/{}".format(niv1,niv2)
		print(url)

		contenu = requests.get(url)
		page = BeautifulSoup(contenu.text,"html.parser")

### Ici, je vais chercher le nombre d'items de chaque page
		for h1 in page.find_all("h1"):
			nb = h1.text.split("(")
			nb = nb[1].split(" ")
			nb = nb[0]
			# print(nb)

### Je m'en sers pour créer une url2 qui permet d'afficher tous les items contenus dans une sous-section sur une seule page
			url2 = "{}?pagesize={}".format(url,nb)
			print(url2)

### J'ouvre cette sous-section avec BeautifulSoup
			contenu2 = requests.get(url2)
			page2 = BeautifulSoup(contenu2.text,"html.parser")
			#print(contenu2)

			produits = page2.find_all("div",class_="product-tile")

			for produit in produits:
				# print(produit)
				n += 1
				prod = []

### Pour chaque produit, je ramasse la marque, le nom, le code de produit et le prix

				try:
					marque = produit.find("strong",class_="product-tile-brand").text.strip()
				except:
					marque = "?"

				try:
					nom = produit.find("div",class_="product-tile-text").a.text.strip()
				except:
					nom = "?"

				try:
					code = produit.find("div",class_="product-tile-text").a["data-productid"]
				except:
					code = "?"

				try:
					prix = produit.find("div",class_="product-tile-price").text.strip()
				except:
					prix = "?"

### J'ajoute à la variable «prod» mon compteur, ainsi que mes noms de section et de sous-section

				prod.append(n)
				prod.append(niv1)
				prod.append(niv2)
				prod.append(code)
				prod.append(nom)
				prod.append(marque)
				prod.append(prix)
				print(prod)

				f2 = open(fichier2, "a")
				xyz = csv.writer(f2)
				xyz.writerow(prod)

### Je vais mettre le reste de ton code en commentaires
### Mais l'essentiel était là

# urldeschaussures = page.find_all("div", class_="product-tile-text")
# # print(urldeschaussures)

# chaussure = []

### Excellent: le code ci-dessous met tous les prix présents dans la page dans une liste. Il y en a 451.
### C'est ce qu'on appelle une «list comprehension». C'est comme une liste qu'on fabrique avec une boucle et qui tient en une ligne de code.

# prix = [x.span.text for x in page.find_all('div', class_='product-tile-price')]
# print(prix)

### Vérification du nombre d'items dans la page
# print(len(prix))

#J'ai vraiment tenter de séparer les prix dans une colonne différente mais je n'ai pas été capable de trouver comment. Avoir le prix a vraiment été complique ( j'ai plusieurs commentaire vers lbas qui le prouve haha)

# for urlchaussure in urldeschaussures:
# 	chaussure =[]

# 	try:
# 		url2 = urlchaussure.a["href"]
# 		url2 = "https://www.sportsexperts.ca" + url2
# 		print(url2)

# 		contenu2 = requests.get(url2)
# 		page2 = BeautifulSoup(contenu2.text,"html.parser")
# 		#print(contenu2)

# 		brand = page2.find("span", class_="product-detail-brand").text
# 		#print(brand)
# 		chaussure.append(brand)

# 		categorie = page2.find("span", class_="product-detail-name").text
# 		#print(categorie)
# 		chaussure.append(categorie)


# 		# prix = page2.find(class_="product-tile-price").find_next("span").text
# 		# print(prix)s

# 		pointure = page2.find("h2", class_ = "h6").text
# 		print(pointure)
# 		# tout = page2.find("div", class_="product-detail").text
# 		# print(tout)
		
	

		# f2 = open(fichier2, "a")
		# xyz = csv.writer(f2)
		# xyz.writerow([chaussure])

	# except:
	# 	print("rien ici")

# prix = [x.span.text for x in page.find_all('div', class_='product-tile-price')]
# print(prix)