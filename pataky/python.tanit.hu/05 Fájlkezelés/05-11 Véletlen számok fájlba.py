
"""
05-11 Véletlen számok fájlba
Feladat leírás:
Generálj 50 véletlen pozitív egész háromjegyű számot és azokat írd ki egy "szamok.txt" fájlba.
Minden szám külön sorba kerüljön.
"""

import os.path
from random import randint
random_list = [randint(100, 999) for _ in range(50)]
numbers = open(os.path.join('szamok.txt'), 'wt')
for n in random_list:
    numbers.write(str(n)+'\n')
numbers.close()
