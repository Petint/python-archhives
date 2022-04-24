"""
01-02 Nagyobb
Feladat leírás:
Olvass be két egész számot. Írd ki a nagyobbat. Ha egyformák, akkor írd ki, hogy egyenlők.
Biztosra vehetjük, hogy egész számot adunk meg.
"""

print("Bekérünk két számot és kiírjuk a nagyobbat.")
du = int(input("Adj meg egy számot: "))
du2 = int(input("Adj meg egy számot: "))
if du > du2:
    print("Az első szám (%i) nagyobb." % du)
elif du < du2:
    print("A második szám (%i) nagyobb." % du2)
else:
    print("A két szám egyenlő.")
