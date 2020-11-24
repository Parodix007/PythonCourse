import json, os

def czytaj_plik():
	with open('pytania.json') as file:
		pytania = json.loads(file.read())
		
	return pytania


plik = czytaj_plik()

print(type(plik))
