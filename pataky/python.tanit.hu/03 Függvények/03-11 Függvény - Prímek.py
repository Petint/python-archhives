"""
Adott egy egész számokat tartalmazó lista - lásd alább.
Állapítsd meg minden egyes eleméről, hogy a három hatványa-e, vagy prím szám és írd ki a mintának megfelelően.
A prím osztók megtalálásához készíts egy függvényt "prim_osztok" néven, amelynek a bemenő paramétere egy egész szám,
a visszatérési értéke pedig egy lista, amely tartalmazza a bejövő szám prím osztóit.
Ha nincs prím osztója a bejövő számnak, akkor üres listát adjon vissza.
"""


def prim_osztok(number):
    divider = 0
    for whatever in range(1, number + 1):
        if number % whatever == 0:
            divider += 1
        if divider > 2:
            return False
    return True


def harom_hatvany(number):
    if number % 3 == 0:
        return True
    else:
        return False



def main():
    lista = [123, 57, 8, 16, 29, 125, 81, 64, 127, 82]
    print('Egy lista elemeiről állapítjuk meg, hogy prímek-e vagy három hatványai.')
    for user_number in lista:
        print(f'{user_number} - prím szám' if prim_osztok(user_number) else (f'{user_number} - három hatványa' if harom_hatvany(user_number) else user_number), sep='')


if __name__ == '__main__':
    main()
