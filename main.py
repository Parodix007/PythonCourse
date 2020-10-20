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





#? I/O w Pythonie

#TODO: funkcja input() przyjmuje argument opcjonalny ktorym jest zazwyczaj string, jest on wyswietlany jako wiadomosc do uzytkownika ktory bedzie wprowadzal wartosc do programu.


input_ = input('Podaj wartosc zmiennej: ')

#TODO: funkcja print() dziala identycznie lecz przyjmuje drugi argument ktorym jest zmienna ktora bedzie wyswietlana w terminalu.

print("wartosc:",input_)


#? Data Types


#? Data Structures

#TODO: list jest w zasadzie typem Tablicy zmiennym dynamicznie

list_ = [1,2,3,4]
# index []
# len()
# append
# insert
# remove

#TODO: jest to typem Tablicy o wartosciach niezmiennych

tuple_ = (1,2,3,4)

#TODO: Jest to struktura danych nazywana takze w czasami tablica asocjacyjna

dict_ = {
    'raz' : 1,
    'dwa' : 2,
    'trzy' : 3
}

# index []
# get
# items

# for x, y in dict_.items():
#     print(f'{x} : {y}')
