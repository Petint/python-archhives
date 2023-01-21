"""Írj függvényt "nagyobbTripla" néven, amely visszaadja a két szám közül a nagyobb háromszorosát."""


def nagyobb_tripla(a, b):
    return 3 * max(a, b)


if __name__ == '__main__':
    print('Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb háromszorosát.')
    aa = int(input("Adj meg egy számot>"))
    bb = int(input("Adj meg egy számot>"))
    print(nagyobb_tripla(aa, bb))
