import json

def read_file():
	with open('pytania.txt') as file:
		pytania = json.loads(file.read())
		print(pytania['pytania']['pytanie1'])



read_file()