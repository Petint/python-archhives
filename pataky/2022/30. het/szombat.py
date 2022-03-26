""""
01-02 Nagyobb
Feladat leírás:
Olvass be két egész számot. Írd ki a nagyobbat. Ha egyformák, akkor írd ki, hogy egyenlők.
Biztosra vehetjük, hogy egész számot adunk meg.
"""

a, b = int(input('Adj meg egy kétjegyű egész számot: ')), int(input('Adj meg egy kétjegyű egész számot: '))
if a == b:
    print('A ket szam egyenlo.')
elif a > b:
    print(a)
else:
    print(b)

"""
01-31 Számolás
Feladat leírás:
Kérjünk be a felhasználótól két darab kétjegyű egész számot. 
Biztosak lehetünk benne, hogy azt ad meg, ezért nem kell ellenőrizni.
Utána írjuk ki a két számmal elvégzett alábbi műveleteket és azok eredményét a minta szerint.
"""

print(f"""
{a}+{b}={a + b}
{a}-{b}={a - b}
{a}*{b}={a * b}
{a}/{b}={a / b}, ket tizedesre kerekitve:  {round(a / b,2)}
""")
