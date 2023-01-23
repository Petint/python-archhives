"""
Olvass be öt egész számot egy beolvasással, a számokat pontosvesszővel és szóközökkel elválasztva. A számok lehetnek negatívak is.
Feltételezhetjük, hogy a megadott minta szerint adja meg a felhasználó a számokat, azt külön nem kell ellenőrizni.
A beolvasott számokat írjuk ki csökkenő sorrendben, dupla kisebb jellel és szóközökkel elválasztva.
A beolvasáshoz és kiíráshoz lásd a mintát.
"""


def main():
    numbers = input('Adj meg 5 egész számor "; "-el elválasztva:')
    numbers = numbers.split('; ')
    numbers = [int(number) for number in numbers]
    numbers = sorted(numbers, reverse=True)
    print('A megadott számok növekvő sorrendben:')
    [print(number, end=' >> ') for number in numbers]


if __name__ == '__main__':
    print('Számokat olvasunk be és rendezve írjuk ki')
    main()
