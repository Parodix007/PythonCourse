import json, os

def czytaj_plik():
	with open('pytania.json') as file:
		pytania = json.loads(file.read())
		
	return pytania



def organizacja_gry(plik_z_pytaniami):
	obiek_pytania = plik_z_pytaniami['pytania']
	odpowiedzi = []
	for pytanie in obiek_pytania:
		os.system('clear')
		print(obiek_pytania[pytanie]['tresc'])
		odpowiedz = input('Wpisz odpowiedz: ')
		odpowiedzi.append(odpowiedz.upper())

	return walidacja(odpowiedzi, obiek_pytania)


def walidacja(lista_odpowiedzi, obiek_z_pytaniami):
	i=0
	wynik = 0
	for obiekt in obiek_z_pytaniami:
		if lista_odpowiedzi[i] == obiek_z_pytaniami[obiekt]['poprawna']:
			wynik+=1
		i+=1

	print(f'Uzyskales: {wynik} na {len(lista_odpowiedzi)} pkt')

	

	


plik = czytaj_plik()

organizacja_gry(plik)