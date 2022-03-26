""""
01-02 Nagyobb
Feladat leírás:
Olvass be két egész számot. Írd ki a nagyobbat. Ha egyformák, akkor írd ki, hogy egyenlők.
Biztosra vehetjük, hogy egész számot adunk meg.
"""

a, b = int(input('Addj meg egy szamot: ')), int(input('Addj meg egy szamot: '))
if a == b:
    print('A ket szam egyenlo.')
elif a > b:
    print(a)
else:
    print(b)



