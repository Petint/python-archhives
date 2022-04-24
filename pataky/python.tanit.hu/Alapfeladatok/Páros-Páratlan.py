"""
01-03 Páros-páratlan
Feladat leírás:
Olvassunk be egy egész számot.
Ha nem egész szám, akkor írjuk ki, hogy "Nem egész szám", különben írjuk ki, hogy páros-e vagy páratlan.
"""

print("Bekérünk egy számot, és megmondjuk hogy páros-e.")
du = int(input("Adj meg egy számot: "))
if du % 2 == 0:
    print("Ez a szám páros.")
else:
    print("ez a szám páratlan.")

