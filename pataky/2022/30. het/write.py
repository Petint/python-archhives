import os.path
from random import randint

"""
05-11 Véletlen számok fájlba
Feladat leírás:
Generálj 50 véletlen pozitív egész háromjegyű számot és azokat írd ki egy "szamok.txt" fájlba.
Minden szám külön sorba kerüljön.
"""
random_list = [randint(100, 999) for _ in range(50)]
numbers = open(os.path.join('szamok.txt'), 'wt')
for n in random_list:
    numbers.write(str(n)+'\n')
numbers.close()

"""
05-12 Páratlan számok fájlbaFeladat leírás:
Olvass be egész számokat addig amíg 0-át nem írnak be.
Ha páratlan számot adtak meg, akkor azt írd ki a "paratlan.txt" fájlba, mindegyik számot külön sorba.
Ha nem egész számot adnak meg, vagy nem páratlan a szám, akkor azt hagyjuk figyelmen kívül és kérjük a következőt.
"""

run = True
odd_file = open('paratlan.txt', 'wt')
while run:
    try:
        du = int(input('Enter a number: '))
    except ValueError:
        pass
    else:
        if du == 0:
            run = False
        elif du % 2:
            odd_file.write(str(du) + '\n')
        else:
            pass
odd_file.close()
