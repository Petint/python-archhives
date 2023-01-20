"""
Olvassunk be egy egész számot és írjuk ki hogy prímszám-e.
Abban biztosak lehetünk, hogy a felhasználó egynél nagyobb egész számot ad meg.
"""


def is_prime():
    print(number)
    return False


print('Egy beolvasott számról állapítjuk meg, hogy prím-e')
number = int(input('Adj meg egy számot:'))
print('A ', number, ' ' if is_prime() else ' nem ', 'prímszám', sep='')
