def paratlan(ix: int) -> bool:
    """
      Írj egy függvényt "paratlan" néven, amely bool értéket ad vissza. Bemenő paramétere egy egész szám.
      True-t ad vissza, ha a bemenő paraméter páratlan.
      False-t ad vissza, ha páros. Hibára fut, ha a bejövő paraméter nem szám.
    """
    return ix % 2 != 0


def szorzat(a: int, b: int) -> int:
    """
        Írj egy függvényt "szorzat" néven, amely két számot vár paraméterül és visszaadja a szorzatukat.
        Ha nem számot adak meg, fusson hibára!
    """
    if type(a).__name__ == "int" and type(b).__name__ == "int":
        return a * b
    else:
        raise TypeError


def kisebb_dupla(a: int, b: int) -> int:
    """
        Írj egy függvényt "kisebbDupla" néven, amely két számot kap paraméterül
        és visszaadja a kisebb szám dupláját.
    """
    return 2 * min(a, b)


def kor(r: float):
    from math import pi
    print(f"A kor kerulete: {round(2 * r * pi, 2)} cm")
    return round(r**2*pi, 2)


def maganhangzo(char: chr) -> bool:
    if char in 'uioaUIOA':
        return True


if __name__ == '__main__':
    for x in range(10):
        print(x, end=' ')
        print('paratlan') if paratlan(x) else print('pasros')
    print("")
    print(szorzat(2, 2))
    print("")
    print(kisebb_dupla(3, 7))
    radx = float(input("Add meg egy kor sugarat: "))
    print(f'A kor terulete: {kor(radx)} cm²')
    print('maganhangzo') if maganhangzo('a') else print('massalhangzo')

