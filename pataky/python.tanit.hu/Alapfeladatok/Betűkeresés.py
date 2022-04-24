"""
01-07 Betűkeresés
Feladat leírás:
Olvassunk be egy szöveget és írjuk ki, hogy van-e benne kis "a"-betű
"""
print("Bekérünk egy szöveget és megállapítjuk, hogy van-e benne \'a\' betű.")
du = input("Adj meg egy szöveget: ").lower()
if 'a' in du:
    print("A szöveg tartalmaz \'a\' betűt.")
else:
    print("A szöveg nem tartalmaz \'a\' betűt.")
