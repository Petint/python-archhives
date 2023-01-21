"""
Írj egy függvényt "szorzat" néven, amely két számot vár paraméterül és visszaadja a szorzatukat.
Ha nem számot adnak meg, fusson hibára!
"""


def szorzat(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':
    print('Egy függvényt tesztelünk, amely két szám szorzatát adja vissza eredményül.')
    aa = int(input("Adj meg egy számot> "))
    bb = int(input("Adj meg egy számot> "))
    print(szorzat(aa, bb))
