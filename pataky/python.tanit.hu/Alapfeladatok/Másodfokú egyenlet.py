"""
01-27 Másodfokú egyenlet
Feladat leírás:
Kérd be a másodfokú egyenlet három paraméterét, az a, b és c együtthatókat.
Biztosra vehetjük, hogy egész számokat adnak meg.
Írd ki a megoldásokat: ha van két megoldás, akkor azokat, ha csak egy akkor azt és azt is írjuk ki, ha nincs megoldás a valós számok halmazán.
"""
import math

a, b, c = float(input("Adj meg egy számot: ")), float(input("Adj meg egy számot: ")), float(input("Adj meg egy számot: "))
answers = 2
try:
    x1 = (b + math.sqrt(b ** 2 - 4 * a * c)) / 2
except ValueError:
    x1 = None
    answers -= 1
try:
    x2 = (b - math.sqrt(b ** 2 - 4 * a * c)) / 2
except ValueError:
    x2 = None
    answers -= 1

if answers == 2:
    megoldasszoveg = f"Két megoldás:\nx1 = {round(x1, 3)}\nx2 = {round(x2, 3)}"
elif answers == 1:
    if x1 is not None:
        megoldasszoveg = f"Egy megoldás:\nx = {round(x1, 3)}"
    else:
        megoldasszoveg = f"Egy megoldás:\nx = {round(x2, 3)}"
else:
    megoldasszoveg = "Nincsen megoldás a valós számok halmazán."

print(megoldasszoveg)
