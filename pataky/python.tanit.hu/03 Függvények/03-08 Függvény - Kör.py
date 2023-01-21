"""
Kérjük be a felhasználótól egy kör sugarát, cm-ben értve.
Feltételezhetjük, hogy a felhasználó valóban számot ad meg, de az lehet tört szám is.
Írj két saját függvényt a kör adatainak a kiszámításához.

Az egyik függvény neve 'kerulet' legyen, bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör kerületét és írja is ki az eredményt a konzolra a minta szerint, cm-ben.

A másik függvény neve 'terulet' legyen, bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör területét és adja vissza az eredményt.
A szöveges, minta szerinti cm²-ben számolt kiírást a főprogramban hajtsuk végre.

Az eredményeket mindkét esetben 2 tizedesre kerekítsük.
"""
from math import pi


def kerulet(radius: float):
    print('A kör kerülete:', round(2 * radius * pi, 2), 'cm')


def felulet(r: float) -> float:
    return (r ** 2) * pi


if __name__ == '__main__':
    print('Egy kor keruletet es feluletet fogjuk meghatarozni.')
    sugar = float(input('Add meg a kor sugarat: ').replace(',', '.'))
    kerulet(sugar)
    print('A kor felulete: %.2f cm²' % (felulet(sugar)))
