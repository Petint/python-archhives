"""
Feladat leírás:
Kérjük be a felhasználótól egy egyenlő oldalú háromszög oldalhosszát, cm-ben értve.
Feltételezhetjük, hogy a felhasználó valóban számot ad meg, de az lehet tört szám is.
Írj két saját függvényt a egyenlő oldalú háromszög adatainak a kiszámításához.

Az egyik függvény neve 'kerulet' legyen, bemenő paramétere a egyenlő oldalú háromszög oldala cm-ben.
A függvény számolja ki a háromszög kerületét és írja is ki az eredményt a konzolra a minta szerint, cm-ben.

A másik függvény neve 'terulet' legyen, bemenő paramétere a néygzet oldalhossza cm-ben.
A függvény számolja ki a egyenlő oldalú háromszög területét és adja vissza az eredményt.
A szöveges, minta szerinti cm²-ben számolt kiírást a főprogramban hajtsuk végre.

Az eredményeket mindkét esetben 2 tizedesre kerekítsük.
"""
import math


def main():
    print('Egy egyenlő oldalú háromszög oldalhosszát kérjük be\nés kiírjuk a kerületét cm-ben és a területét cm²-ben.')
    side = float(input('Add meg az egyik oldalhosszát cm-ben:'))
    kerulet(side)
    print('Az egyenlő oldalú háromszög területe: %.2f cm²' % (terulet(side)))


def kerulet(oldal):
    print('Az egyenlő oldalú háromszög kerülete: %.2f cm' % (3 * oldal))


def terulet(side):
    return side * (math.sqrt(3) * side / 2) / 2


if __name__ == '__main__':
    main()
