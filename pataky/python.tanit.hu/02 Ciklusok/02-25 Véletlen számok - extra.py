"""
Generálj le 30 db véletlen kétjegyű egész számot.
Írd ki a sorozatot emelkedő sorrendben, majd a max, min és átlagukat.
Az átlag számításánál az azonos számokat csak egy elemként vegyük figyelembe. Az egyedi elemeket tartalmazó sorozatot is írjuk ki.
Azaz például ha öt számról lenne szó, amelyek 2, 3, 4, 4, 4, akkor itt a 2, 3, 4 átlagát kell számolni.
"""
from random import randint
print('Legenerálunk 30 kétjegyű véletlen egész számot, majd kiírjuk emelkedő sorrendben, a legnagyobb és a lrgkisebb értéket')
numbers = [randint(10, 99) for _ in range(30)]
print('A sorozat: ')
for number in sorted(numbers):
    print(number, end='\t')
print('')
print('A számok közül a legnagyobb:', max(numbers))
print('A számok közül a legkisebb:', min(numbers))
print('A számok átlaga:', sum(numbers)/len(numbers))
