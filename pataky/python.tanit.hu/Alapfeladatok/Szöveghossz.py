"""
01-04 Szöveghossz
Feladat leírás:
Olvass be két szöveget és írd ki a rövidebbet. Ha egyforma hosszúak, akkor írd ki, hogy egyformák.
"""
print("Bekérünk két szöveget és kiírjuk a hosszabb.")
du = input("Adj meg egy szöveget: ")
du2 = input("Adj meg egy szövegot: ")
if len(du) > len(du2):
    print("Az első szöveg (%s) hosszabb." % du)
elif len(du) < len(du2):
    print("A második szöveg (%s) hosszabb." % du2)
else:
    print("A két szöveg hossza egyenlő.")
