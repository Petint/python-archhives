"""
Gagyimatek V2
A négy alapművelet + hatványozás gagyi változata:
Csak össeadással meg kivonással.
"""


__all__ = ['osszead', 'kivon', 'szorzat', 'oszt', 'hatvany']

"""Műveletek"""
def osszead(a, b):
    """A két beadott szám össege
    (a+b)
    """
    return a + b


def kivon(a, b):
    """A két beadott szám külombsége (a-b)"""
    return a - b


def szorzas(a, b):
    """Összeszoroz két számot, de gagyin (a*b)"""
    _eredmeny = 0
    for x in range(a):
        _eredmeny = osszead(_eredmeny, b)
    return _eredmeny

def oszt(a, b):
    """A világ legrosszabb osztómetódusa (a/b)"""
    if b == 0: raise TypeError("Nullahiba")
    _eredmeny = 0
    while a > 0:
        a = kivon(a, b)
        _eredmeny = osszead(_eredmeny, 1)
    return _eredmeny


def hatvany(a, b):
    """Az első szám hatványraemelése (a^b)"""
    if b == 0: return 1
    _eredmeny = a
    for x in range(b-1):
        _eredmeny = szorzas(_eredmeny, a)
    return _eredmeny


if __name__ == "__main__":
    print(osszead(5, 5))
    print(kivon(5, 5))
    print(szorzas(5, 5))
    print(oszt(5,5))
    print(hatvany(5, 5))
    print(__all__)
    input()
