# w
# r
# a
# w+/r+

# file = open('files/test.txt', 'w+')

# print(file.readlines())

# file.write('dane wpisane do pliku')

# print(file.readlines())

# file.close()

# with open('files/test.txt', 'r') as file:
# 	print(f"test.txt: {file.closed}")
# 	print(file.read())


# with open('files/test1.txt', 'w+') as file:
# 	file.write('test1')
# 	print(file.read())
# 	print(f'test1: {file.closed}')

# Cykliczne tablice 

with open('files/cykliczne_tablice.txt', 'r+') as file:
	print(file.readlines())