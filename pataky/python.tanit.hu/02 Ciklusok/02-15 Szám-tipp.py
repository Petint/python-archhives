"""
Generáljunk egy véletlen egyjegyű számot. Kérjünk meg a felhasználót, hogy tippelje meg.
Max 5 tippje lehet. Ha eltalált, akkor írjuk ki, hogy "Talált!".
Ha 5 próbából nem találja el, írjuk ki, hogy "Nem talált!".
Abban biztosak lehetünk, hogy mindig egész számot ad meg.
Minden esetben írd ki a program végén, hogy "Viszlát!"
"""
from random import randint
secret_number = randint(0, 9)
print('Ki kell találnod egy egyjegyű véletlen számot. Max ötöt tippelhetsz')
for i in range(5):
    dear_user = int(input('Tippeld meg a számot: '))
    if dear_user == secret_number:
        print('Talált!')
        break
    print('Sajnos nem talált!')
    print('Nincs több próbálkozási lehetőséged.') if i == 4 else print('Próbáld újra!')
print('Viszlát!')
