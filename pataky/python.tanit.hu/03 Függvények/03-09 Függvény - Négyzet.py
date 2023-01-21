"""
Kérjük be a felhasználótól egy négyzet oldalhosszát, cm-ben értve.
Feltételezhetjük, hogy a felhasználó valóban számot ad meg, de az lehet tört szám is.
Írj két saját függvényt a négyzet adatainak a kiszámításához.

Az egyik függvény neve 'kerulet' legyen, bemenő paramétere a négyzet oldala cm-ben.
A függvény számolja ki a négyzet kerületét és írja is ki az eredményt a konzolra a minta szerint, cm-ben.

A másik függvény neve 'terulet' legyen, bemenő paramétere a néygzet oldalhossza cm-ben.
A függvény számolja ki a négyzet területét és adja vissza az eredményt.
A szöveges, minta szerinti cm²-ben számolt kiírást a főprogramban hajtsuk végre.

Az eredményeket mindkét esetben 2 tizedesre kerekítsük.
"""


def kerulet(a):
    print('A négyzet kerülete:', round(4 * a, 2), 'cm')


def felulet(a):
    return a ** 2


if __name__ == '__main__':
    print('Egy négyzet keruletet es feluletet fogjuk meghatarozni.')
    sugar = float(input('Add meg a negyzet egyik oldalának hosszát:').replace(',', '.'))
    kerulet(sugar)
    print('A négyzet területe: %.2f cm²' % (felulet(sugar)))
