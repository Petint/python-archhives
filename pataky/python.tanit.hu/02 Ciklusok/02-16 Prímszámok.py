"""
Olvassunk be egy egész számot és írjuk ki hogy prímszám-e.
Abban biztosak lehetünk, hogy a felhasználó egynél nagyobb egész számot ad meg.
"""


def is_prime():
    divider = 0
    for whatever in range(1, number + 1):
        if number % whatever == 0:
            divider += 1
    return divider == 2


print('Egy beolvasott számról állapítjuk meg, hogy prím-e')
number = int(input('Adj meg egy számot:'))
print('A ', number, ' ' if is_prime() else ' nem ', 'prímszám', sep='')
