"""
Írj egy függvényt "kisebbDupla" néven, amely két számot kap paraméterül és visszaadja a kisebb szám dupláját.
"""


def kisebb_dupla(a: int, b: int) -> int:
    return 2 * min(a, b)


if __name__ == '__main__':
    aa = int(input("Adj meg egy számot>"))
    bb = int(input("Adj meg egy számot>"))
    print(kisebb_dupla(aa, bb))
