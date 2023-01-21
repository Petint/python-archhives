"""
Generálj le 10 db véletlen kétjegyű egész számot.
Írd ki a sorozatot emelkedő sorrendben.
Számold ki az átlagukat kétféleképpen:
a) a Python beépített függvényeit használva
b) ciklust használva
"""
from random import randint
print('Legenerálunk 10 kétjegyű véletlen számot, majd kiírjuk az átlagukat, amelyt kétféleképpen számolunk ki.\n'
      'a) a Python függvényeivel; b) ciklussal')
numbers = [randint(10, 99) for _ in range(10)]
print('A sorozat: ')
for number in sorted(numbers):
    print(number, end='\t')
print('')
foo = 0
for bar in numbers:
    foo += bar
average = foo / 10
print('a) A sorozát átlaga Python függvényekel:', sum(numbers)/len(numbers))
print('b) A számok átlaga ciklussal számolva:', average)
