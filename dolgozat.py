def feladat1():
    """
        1. feladat: Kérjen be ellenőrzötten egész számokat a felhasználótól,
        amíg érvényes bemenetet ad, majd írja ki az utolsó lefutásnál a minimumát ezeknek!
    """
    valid_nums = []
    is_valid = True
    while is_valid:
        du = input("Adj meg egy számot: ")
        if du.isnumeric():
            valid_nums.append(int(du))
        else:
            is_valid = False
    try:
        print(f"A legkisebb szám: {min(valid_nums)}")
    except ValueError:
        print("Nem adtál meg számot.")


def feladat2():
    """
        2. feladat: Számolja össze, majd írja ki, hogy hány darab páratlan háromjegyű szám van!
    """
    paratlan_szamok = [i for i in range(101, 1001, 2)]
    print(len(paratlan_szamok))


def feladat3():
    """
        3. feladat: Számolja össze, majd írja ki, hogy hány darab páros négyjegyű szám van!
    """
    paros_szamok = [i for i in range(1000, 10000, 2)]
    print(len(paros_szamok))


def feladat4():
    """
        4. feladat: A kapott listát összegezze és átlagolja, ezeket írja is ki!
    """
    lista = [18, 21, 45, 37, 92, 65, 83, 39]
    print(f"""
A lita összege: {sum(lista)}
A lisza átlaga: {sum(lista) / len(lista)}
    """)


def feladat5():
    """
        5. feladat: A kapott listából másolja ki egy másik listába az hárommal osztható számokat,
        majd ELEMENKÉNT írja is ki a végeredményt!
    """
    lista = [18, 21, 45, 37, 92, 65, 83, 39]
    harommal_oszthato = []
    for e in lista:
        if e % 3 == 0:
            harommal_oszthato.append(e)
    for i in harommal_oszthato:
        print(i, end="\t")
    else:
        print('')


def feladat6():
    """
        bónusz feladat: Egy listába gyűjtse ki az első 10 darab,
        tíznél nagyobb prímszámot, és írja ki a legkisebbet és a legnagyobbat!
    """
    primes = [2, 3, 4, 5, 7]  # A programnak nem kell ezeket megtalálnia, ez gyorsítsa és egyszerüsíti a programot.
    nums_to_test = [i for i in range(11, 1001, 2)]
    for i in nums_to_test:
        is_prime = True
        for j in primes:
            is_prime = not (i % j == 0)
            if not is_prime:
                break
        if is_prime:
            primes.append(i)
    valid = primes[5:15]
    for v in valid:
        print(v, end=", ")
    else:
        print('')
    # print(nums_to_test)


if __name__ == "__main__":
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
