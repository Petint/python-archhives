"""
Írj egy függvényt "parosParatlan" néven, amely a bejövő paraméter alapján kiírja, hogy az páros-e vagy páratlan. Pl. így: Ez a szám ... páros!
"""


def paros_paratlan(num: int):
    print('Ez a szám pár', 'atlan' if bool(num % 2) else 'os', ': ', aa, sep='')


if __name__ == '__main__':
    print('Egy függvényt tesztelünk, amely egy egész számról mondja meg, hogy páratlan-e')
    aa = int(input('Adj meg egy számot:'))
    paros_paratlan(aa)
