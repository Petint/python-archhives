"""
01-05 Nagyobb 10-nél
Feladat leírás:
Olvass be egy egész számot. Írd ki ha nagyobb tíznél: "Nagy", különben azt, hogy "Kicsi".
Biztosra vehetjük, hogy egész számot adunk meg.
"""
print("Megálapítjuk egy számról hogy nagyobb-e 10-nél.")
du = int(input("Adj meg egy számot: "))

if du > 10:
    print("Nagy")
else:
    print("Kicsi")
