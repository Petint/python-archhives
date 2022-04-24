"""
01-06 Szám duplája
Feladat leírás:
Olvassunk be egy egész számot.
Ha nem egész számot adtak meg, érjen véget azzal, hogy kírjuk: "HIBA: Nem egész számot adtál meg!".
Különben írjuk ki a szám dupláját.
"""

# Hibakezeléses számbekérés
try:
    du = int(input("Adj meg egy számot: "))
except ValueError:
    print("HIBA: Nem egész számot adtál meg!")
else:
    print(2 * du)
