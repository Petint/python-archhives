"""
01-01 Szöveg-szám
Feladat leírás:
Olvassunk be egy számot. Ha nem egész szám, akkor írjuk ki, hogy "Nem egész szám", különben írjuk ki, hogy "Egész szám".
Végeredmény minta (részlet):
"""

print("Megálapítjuk hogy számot egész számot adtál-e meg.")
du = input("Adj meg egy számot: ")
if du.isnumeric():
    print("Ez egy egész szám.")
else:
    print("Ez nem egy egész szám.")
