from multiprocessing import Pool
from random import randint
# Ropogós
"""
Feladat leírás:
Adott az alábbi adatsor. Írjuk ki, hogy hány egyjegyű, hány kétjegyű és hány háromjegyű szám van benne.
"""
# adatsor = (210, 23, 124, 3, 5, 567, 56, 87, 9, 7, 3, 45, 678, 543, 24, 3, 567, 2, 1, 12, 48, 9, 12, 345, 64, 87, 84, 347, 56, 2, 3, 14, 578, 93, 432, 34, 567, 43)
adatsor = (randint(-999, 999) for _ in range(1000000000))
count1 = 0
count2 = 0
count3 = 0


def eval(i:int):
    global count1, count2, count3
    i = abs(i)
    if i < 10:
        count1 += 1
    elif i < 100:
        count2 += 1
    elif i < 1000:
        count3 += 1


"""
for i in adatsor:
    eval(i)
    print("▓",end='')
else:
    print('')
"""

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(eval, adatsor)
    print(count1, count2, count3, sep="\n")

