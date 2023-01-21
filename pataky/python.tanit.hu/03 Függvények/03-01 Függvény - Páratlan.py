"""
Írj egy függvényt "paratlan" néven, amely bool értéket ad vissza.
Bemenő paramétere egy egész szám.
True-t ad vissza, ha a bemenő paraméter páratlan. False-t ad vissza, ha páros.
Hibára fut, ha a bejövő paraméter nem szám.
A függvény teszteléséhez a főprogram kérjen be egy egész számot a felhasználótól.
A program kommunikációja a mintának megfelelően történjen.

"""


def paratlan(num: int) -> bool:
    return bool(num % 2)


if __name__ == '__main__':
    print('Egy függvényt tesztelünk, amely egy egész számról mondja meg, hogy páratlan-e')
    number = int(input('Adj meg egy számot:'))
    print('Ez a szám pár', 'atlan' if paratlan(number) else 'os', ': ', number, sep='')
