"""
01-19 ABC sorrend
Feladat leírás:
Olvass be két angol nevet a konzolról és írd ki, melyik van előbb a névsorban.
Pl. a végén ezt írd ki: David előbb van a névsorban mint Marcus.
"""
print("Megállapítjuk, hogy melyik név van előbb a névsorban.")
du = input("Adj meg egy angol nevet: "), input("Adj meg egy angol nevet: ")
name1, name2 = min(du), max(du)
print(f"{name1} előbb van a névsorban mint {name2}")
