"""
Feladat leírás:
Adott a BP_homerseklet.txt fájl, amely utf-8 kódolással tartalmazza Budapest éves hőmérsékleti adatait, pontosvesszőkkel elválasztva.
A fájl az alábbi fejlécet és adatokat tartalmazza: #ev;kozepho;maxho;maxho_nap;minho;minho_nap
Fejléc elemek magyarázata:
ev - évszám
kozepho - évi középhőmérséklet
maxho - a legmagasabb napi középhőmérséklet az évben
maxho_nap - a legmagasabb napi középhőmérséklet napja
minho - a legalacsonyabb napi középhőmérséklet az évben
minho_nap - a legalacsonyabb napi középhőmérséklet napja

1. feladat: Írjunk egy "beolvas" függvényt a fájl adatainak listába történő belvasására.
2. feladat: Ellenőrizzük, hogy minden év adata megvan-e a fájlban 1901-től 2020-ig (ez 120 adat).
Ha megvan minden adat, akkor írjuk ki, hogy: "Minden év adata megvan 1901-től 2020-ig."
Különben írjuk ki, hogy: "Hiányos a fájl, nincs meg minden adat 1901-től 2020-ig."
3. feladat: Írjuk ki azokat az éveket, amelyekben Karácsony napján (december 25-én) volt a leghidegebb.
4. feladat: Keressük meg azt az évet, amelyben a legnagyobb volt a minimális és maximális hőmérséklet közti különbség.

Az adatok forrása:
https://www.met.hu/eghajlat/magyarorszag_eghajlata/eghajlati_adatsorok/Budapest/adatok/eves_adatok/
"""


