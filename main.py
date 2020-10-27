import os

print('Witamy na kursie Python!!!')
print('Prowadze przez: Sebastiana Siarczyńskiego')

#os.system('clear')

#? Przyklad deklaracji zmiennej w Pythonie

zmienna = 100

#? Przyklad If`a w Pythonie

x = True

if x:
    print('Cos tam') 

#? Przyklad For i While w Pythonie
a = 1


while a < 5:
    print('cos tam')
    a += 1



for i in range(5):
    print(i)




#? FizzBuzz

fb = 3

if fb % 3 == 0:
    print('Fizz')
elif fb % 5 == 0:
    print('Buzz')
elif fb % 5 == 0 and fb % 3 == 0:
    print('FizzBuzz')

os.system('clear')

for item in range(10):
    if item % 3 == 0:
        print('Fizz')
    elif item % 5 == 0:
        print('Buzz')
    elif item % 5 == 0 and fb % 3 == 0:
        print('FizzBuzz')

os.system('clear')

b = 0
while b < 10:
    if b % 3 == 0:
        print('Fizz')
    elif b % 5 == 0:
        print('Buzz')
    elif b % 5 == 0 and fb % 3 == 0:
        print('FizzBuzz')
    b +=1
 


#? I/O w Pythonie

#TODO: funkcja input() przyjmuje argument opcjonalny ktorym jest zazwyczaj string, jest on wyswietlany jako wiadomosc do uzytkownika ktory bedzie wprowadzal wartosc do programu.
os.system('clear')

#input_ = input('Podaj wartosc zmiennej: ')


#TODO: funkcja print() dziala identycznie lecz przyjmuje drugi argument ktorym jest zmienna ktora bedzie wyswietlana w terminalu.

#print("wartosc:",input_)

os.system('clear')

#? Data Types


#? Data Structures

#TODO: list jest w zasadzie typem Tablicy zmiennym dynamicznie

list_ = [1, 2, 3, 4, True, 'sadas']

print(list_[0])
# index []
# len()
# append
list_.append('costam')
print(list_)
# insert
list_.insert(1, 1234)
print(list_)
# remove
list_.remove(2)
print(list_)



os.system('clear')



# fiblist = [1,1]
# n = 20

# for item in range(n):
#     fiblist.append(fiblist[-1] + fiblist[-2])

# print(fiblist)


lista1 = [10,20,30,20,60,100,120,20,30,80,60]
lista2 = []

for item in lista1:
    if item not in lista2:
        lista2.append(item)

print(lista2)


#TODO: jest to typem Tablicy o wartosciach niezmiennych

#tuple_ = (1,2,3,4)









#TODO: Jest to struktura danych nazywana takze w czasami tablica asocjacyjna

# dict_ = {
#     'raz' : 1,
#     'dwa' : 2,
#     'trzy' : 3
# }

# index []
# get
# items

# for x, y in dict_.items():
#     print(f'{x} : {y}')
