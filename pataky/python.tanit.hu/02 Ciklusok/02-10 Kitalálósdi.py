"""
A felhasználó tippeljen meg egy véletlen egész számot amely 1-5 között van. Addig tippelhet, amíg el nem találja.
Ha nem egész számot ad meg, akkor írjuk ki, hogy ez nem egész szám, és tippelhet tovább.
Érjen véget a program, ha eltalálja a véletlen számot, vagy ha üres sztringet ad meg.
Minden esetben írd ki a program végén, hogy "Viszlát!"
"""
from random import randint
secret_number = randint(1, 5)

print('Ki kell találnod egy 1-5 véletlen számot. Ha nemn akarsz tippelni csak nomj sima entert.')
tip = -1
while tip != secret_number:
    try:
        tip = int(input('Tippeld meg a számot (1-5 között): '))
    except ValueError:
        break
    if tip == secret_number:
        print('Gratulálok, eltaláltad!')
print('Viszlát!')
