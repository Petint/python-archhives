"""
1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját Ultrabalaton néven mentse el!
2. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el egy olyan adatszerkezetben, ami a további feladatok megoldására alkalmas! Az állományban legfeljebb 500 sor lehet.
3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány egyéni sportoló indult el a versenyen!
4. Számolja meg és írja ki a képernyőre a minta szerint, hogy hány női sportoló teljesítette a teljes távot!
5. Kérje be a felhasználótól egy sportoló nevét, majd határozza meg és írja ki a minta szerint, hogy a sportoló indult-e a versenyen! A keresést ne folytassa, ha az eredményt meg tudja határozni! Ha a sportoló indult a versenyen, akkor azt is írja ki a képernyőre, hogy a teljes távot teljesítette-e! Feltételezheti, hogy nem indultak azonos nevű sportolók ezen a versenyen.
6. Készítsen IdőÓrában azonosítóval valós típusú értékkel visszatérő függvényt vagy jellemzőt, ami a versenyző időeredményét órában határozza meg! Egy óra 60 percből, illetve 3600 másodpercből áll.
7. Határozza meg és írja ki a minta szerint a teljes távot teljesítő férfi sportolók átlagos idejét órában! Feltételezheti, hogy legalább egy ilyen sportoló volt.
8. Keresse meg a női és a férfi kategóriák győzteseit és írja ki nevüket, rajtszámukat és időeredményeiket a minta szerint! Feltételezheti, hogy egyik kategóriában sem alakult ki holtverseny és mindkét kategóriában volt célba érkező futó.
"""

import csv
from curses import raw
"""import pandas as pd


def opendata(filename: str):
    csvfile = pd.read_csv(filename, sep=';')
    return csvfile

"""


def opendata(filename: str):
    file = open(filename, newline='\n')
    raw_data = csv.reader(file, delimiter=";")
    data = []
    for row in raw_data:
        data.append(str(row).split(';'))
    return data


def egyeni_indulok(_dta):
    indulok = _dta.count()
    return indulok[0]


def beero_nok(_dta):

        return 1

# pd.set_option("display.max_columns", 500)
data = opendata("ub2017egyeni.txt")

# print(data)
print(f"3. feladat: Egyéni indulók: {egyeni_indulok(data)} fő")
print(f"4. feladat: Célba érő női sportolók: {beero_nok(data)}")
