"""Miscs"""


def min_max_atlag(nums):
    larg, smal = max(nums), min(nums)
    avrg = sum(nums) / len(nums)
    print(f"A számok átlaga: {avrg}\nA legkisebb szám: {smal}\nA legnagyobb szám: {larg}")


# 01-01
def Szovegszam(num: str):
    """
        Olvassunk be egy számot.
        Ha nem szám, akkor írjuk ki, hogy "Nem szám", különben írjuk ki, hogy "Szám".
    """

    if num.isnumeric():
        print("Ez egy szám.")
    else:
        print("Ez nem szám.")


# 01-02
def Szamoktipusa(num: str):
    """
        Olvass be egy szöveget.
        Írd ki, hogy egész számot vagy tört számot adtak-e meg.
    """

    if num.isnumeric():  # isinstance(num,int):
        print("Ez egy egész szám.")
    else:
        try:
            int(num)
        except ValueError:
            print("Ez egy tört szám.")
        else:
            print("Ez valami más.")


# 01-02b
def Szamoktipusb():
    data_list = [12, 34.5, True, 'abc', (2, 3), {5, 6, 7}, ['a', 3, 4], {'Name': 'Alfa', 'age': 15}, None]
    for i in data_list:
        print(type(i).__name__)


# 01-03
def Nagyobb(a: int, b: int):
    """
        Olvass be két számot.
        Írd ki a nagyobbat.
    """
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("=")


# 01-04. Páros-páratlan
def Parosparatlan(num: str):
    """
        Olvassunk be egy számot.
        Ha nem szám, akkor írjuk ki, hogy "Nem szám", különben írjuk ki, hogy páros-e vagy páratlan.
    """
    try:
        num = int(num)
    except ValueError:
        print("Nem szám.")
    else:
        if parity(num):
            print("Páros")
        else:
            print("Páratlan")


# 1-05. Szöveghossz
def Soveghoszz():
    """
        Olvass be két szöveget és írd ki a rövidebbet.
    """
    txta = input("Adj meg egY szöveget: ")
    txtab = input("Adj meg egY szöveget: ")
    if txta > txtab:
        print(txta)
    elif txtab > txta:
        print(txtab)
    else:
        print("=")


# 01-06. Nagyobb 10-nél
def Nagyobb10(num: int):  # Nice
    """
        Olvass be egy számot.
        Írd ki ha nagyobb tíznél: "nagy", különben "kicsi".
    """
    if num > 10:
        print("Nagy")
    else:
        print("Kisci")


# 01-07. Szám duplája
def Dupla():
    """
        Olvassunk be egy számot.
        Ha nem számot adtak meg, érjen véget a program egy hibaüzenettel.
        Különben írja ki a szám dupláját.
    """

    try:
        num = int(input("Adj meg egy számot: "))
    except ValueError:
        raise TypeError("Nem számot adtál meg")
    return 2 * num


# 01-08. Betűkeresés
def Betukereso():
    """
        Olvassunk be egy szöveget és írjuk ki, hogy van-e benne "a"-betű.
    """
    bhv = input("Adj meg egy söveget: ")
    apee = bhv.count("a")
    print(f"Az adott sövegben {apee} 'a' betű található.")


# 01-09. Legkisebb
def Legkisebb(n: int) -> int:
    """
        Kérjük be hány számot akar megadni a felhasználó majd annyi számot beolvastatunk és aztán kiírjuk a legkisebbet.
    """
    nums = [int(input("Adj meg egy számot: ")) for _ in range(n)]
    _min = nums[0]
    for num in nums:
        if _min > num:
            _min = num
    return _min


# 01-10. Kitalálósdi
def Kitalalosdi():
    """
        A felhasználó tippeljen meg egy véletlen egész számot amely 1-5 között van.
        Addig tippelhet, amíg el nem találja.
    """
    from random import randint
    num = randint(1, 5)
    tipp = -1
    while tipp != num:
        tipp = int(input("Tippelj egy számot: "))
    print("Eltaláltad a számot")


# 01-11. Számsor - számjegyek száma
def Szamsor():
    """
        Olvassunk be egy számot. Amíg nem számot adnak meg, addig lehet próbálni újra.
        Ha üres sztringet ad meg, akkor vége a programnak.
        Minden esetben, amikor számot ad meg, írjuk ki hány jegyű a szám.
    """
    szam = True
    while szam:
        num = input("Adj meg egy számot: ")
        if num == "" or not num.isnumeric():
            szam = False
        else:
            print(f"A szám {num.__len__()} jegyű.")


# 01-12. Véletlen számsor
def Veletlenzamsor():
    """
        Addig generáljunk véletlen egyjegyű számokat, amíg 1-nem lesz.
        A végén írjuk ki, hányadikra jött az 1-es szám.
    """
    from random import randint
    numl = []
    while True:
        n = randint(0, 9)
        numl.append(n)
        if n == 1:
            break
    print(n)


# 01-13. Szám lista és oszthatóság
def lista_es_oszthatosag():
    """
        Készíts egy 5 elemű egész számokat tartalmazó listát.
        Írd ki őket, azzal együtt, hogy oszthatók-e öttel.
    """

    from random import randint
    numlst = [randint(-100, 100) for _ in range(5)]  # Lista létrehozva
    for num in numlst:
        print(f"A szám {num}", end=", ")
        print("5-tel nem oszható.") if num % 5 == 0 else print("5-tel oszható.")
    print('')


# 01-14. Magánhangzók száma
def maganhanguok(_input: str):
    """
        Olvass be egy szöveget és írd ki, hogy hány magánhangzó van benne.
    """
    mghn = 0
    for dingus in _input:
        if dingus in "öüóuioőúaéáűí":
            mghn += 1
    print(f"Az adott szöveg {mghn} magánhangzót tartalmaz.")


# 01-15. Szám-tipp
def szam_tip():
    """
        Generáljunk egy véletlen egy jegyű számot.
        Kérjünk meg a felhasználót, hogy tippelje meg.
        Max 5 tippje lehet. Ha eltalált, akkor írjuk ki, hogy "Talált!".
        Ha 5 próbából nem találja el, írjuk ki, hogy "Nem talált!".
    """

    from random import randint
    secnum = randint(0, 9)
    # print(secnum)
    for x in range(5):
        i = int(input("Adj meg egy számot: "))
        if i == secnum:
            print('Talált!')
            break
        elif x > 4:
            print("Nem talált!")
            break
        else:
            print("Nem talált")


# 01-16. Prímszámok
def primszam():
    """
        Olvassunk be egy számot és írjuk ki hogy prímszám-e.
    """
    num = int(input("Adj meg egy számot: "))
    ostok = 0
    for x in range(1, num + 1):
        if num % x == 0:
            ostok += 1
        if ostok > 2:
            print("Nem prím.")
            break
    if ostok == 2:
        print('Prím.')


# 01-17. Beléptetés
def beleptetes():
    """
        Tároljunk egy azonosító/jelszó párost. A felhasználónak ezt kell kitalálni.
        Ha kitalálta, írjuk ki: Beléptetve. Max 5-ször próbálkozhat.
        Ha nem találta ki ez idő alatt, akkor írjuk ki: Belépés megtagadva.
    """
    import belepteto
    user1 = belepteto.Users("PatakyUser", "Passw0rd")
    user1.login()


# 01-18. Számsor
def szamsor():
    """
        Olvassunk be öt számot.
        A végén írjuk ki melyik a legnagyobb és melyik a legkisebb.
        Írjuk ki a számok összegét és átlagát.
    """
    nums = [int(input("Adj meg egy számot: ")) for _ in range(5)]
    min_max_atlag(nums)


# 01-19. ABC sorrend
def abcsor():
    """
        Olvass be két nevet a konzolról és írd ki, melyik van előbb a névsorban.
        Pl. a végén ezt írd ki: Dávid előbb van a névsorban mint Márton.
        Figyeljünk a magyar ékezetes kis és nagybetűk helyes sorrendjére is.
    """
    nev1 = input("Adj meg egy nevet: ")
    nev2 = input("Adj meg még egy nevet: ")
    if nev1 < nev2:
        print(f"{nev1} előbb van a névsorban mint {nev2}")
    else:
        print(f"{nev2} előbb van a névsorban mint {nev1}")


# 01-20. Névsor-első
def nevsor():
    """
        HIBA: Rossul kezeli az ékezetes betűket
        Olvass be öt nevet és írd ki a névsorban legelsőt.
    """
    nevek: 'list[str]' = [input('Adj meg egy nevet: ') for _ in range(5)]
    legkisebb = min(nevek)
    print(legkisebb)


# 01-21. Szövegsorozat
def szovegsorozat():
    """
        Olvass be szöveget addig, amíg üres sztring nem jön be. A végén írd ki, hogy hány szöveg volt beolvasva.
    """
    run = True
    texts = 0
    while run:
        txt = input("Adj meg egy szöveget (üres szöveg a befejezéshez): ")
        if txt == "":
            run = False
        else:
            texts += 1
    print(f"{texts} söveg volt beolvasva.")


# 01-22. Számok fele
def szamokfele():
    """
        Olvass be számokat, amíg 0 nem jön be.
        Ha nem számot adnak meg, írd ki, hogy az nem szám, ha viszont szám, akkor írd ki a felét.
    """
    while True:
        try:
            num = int(input('Adj meg egy számot: '))
        except ValueError:
            print("Nem számot adtál meg!")
        else:
            if num == 0:
                break
            print(num / 2)


# 01-23. Száz véletlen szám
def veletlenszaz():
    """
        Generálj le 100 db véletlen kétjegyű egész számot és írd ki a max, min és átlagukat.
    """
    from random import randint
    randnums = [randint(10, 99) for _ in range(100)]
    return randnums


# 01-24. Száz véletlen szám - extra
def kiertekeles():
    """
        Generálj le 100 db véletlen kétjegyű egész számot és írd ki a max, min és átlagukat.
        Csak egyszer vegyük figyelembe az ismétlődő számokat.
    """
    rnums = veletlenszaz()
    nums = set(rnums)
    min_max_atlag(nums)

# 01-25. Véletlen számok átlaga
def veletlenatlag(n):
    """
        Kérjük be hány számot generáljunk és ha nem egész számot kapunk, jelezzünk hibát!
        Különben generáljunk le annyi kétjegyű véletlen egész számot és írjuk ki az átlagukat.
    """

    from random import randint
    try:
        rl = [randint(10, 99) for _ in range(int(n))]
    except ValueError or TypeError:
        print("Nem számot adtál meg!")
    else:
        min_max_atlag(rl)

# 01-26. Számolás
def szamolas():
    """
        Kérjünk be két számot.
        Ha nem egész számot adtak meg, akkor írjuk ki, hogy ez nem egész szám és érjen is véget a program.
        Különben írjuk ki a két szám összegét, különbségét, szorzatát és hányadosát.
        A hányadost csak akkor írjuk ki, ha az osztó nem nulla.
    """
    try:
        a = int(input("Adj meg egy számot: "))
        b = int(input("Adj meg egy számot: "))
    except ValueError:
        print("Nem egész számot adtál meg!")
        return None
    else:
        print(f"""
A két szám összege:    {a+b},
A két szám kűlömbsége: {a-b},
A kétszám szorzata:    {a*b},
            """)
        print("Nulla mint nevező") if b == 0 else print("A két szám szorzata:   {a//b}.")


"""
    02. Függvények
    A függvényekkel kapcsolatos feladatoknak külön említés nélkül is 
    minden esetben része a függvény helyes működését ellenőrző teszt környezet megírása is.
"""


# 02-01. Függvény: Páratlan
def parity(num: int) -> bool:
    """
        Írj egy függvényt "paratlan" néven, amely bool értéket ad vissza. Bemenő paramétere egy egész szám.
        True-t ad vissza, ha a bemenő paraméter páratlan.
        False-t ad vissza, ha páros. Hibára fut, ha a bejövő paraméter nem szám.
    """
    return num % 2 == 0


# 02-02. Függvény: Szorzat
def szorzat(a, b) -> int:
    """
        Írj egy függvényt "szorzat" néven, amely két számot vár paraméterül és visszaadja a szorzatukat.
        Ha nem számot adak meg, fusson hibára!
    """
    return int(a) * int(b)


# 02-03. Függvény: Kisebb duplája
def kisebb_dupla(a: int, b: int) -> int:
    """
        Írj egy függvényt "kisebbDupla" néven, amely két számot kap paraméterül és visszaadja a kisebb szám dupláját.
    """
    return min(a, b) * 2

# 02-04. Függvény: Magánhangzó
def maganhangzo(char: str) -> bool:
    """
        Írj egy függvényt "maganhangzo" néven, amely a bejövő betűről megállapítja, hogy az magánhangzó-e.
        Azaz True értékkel tér vissza, ha magángangzó, különben False.
        Dobjunk hibát, ha nem egy betű jön be!
    """
    if len(char) > 1:
        raise ValueError
    else:
        return char.lower() in "öüóeuioőúaéáűí"


# 02-05. Függvény: Páros-páratlan kiírás
def paros_paratlan(n: int):
    """
        Írj egy függvényt "parosParatlan" néven, amely a bejövő paraméter alapján kiírja, hogy az páros-e vagy páratlan.
        Pl. így: Ez a szám ... páros!
    """
    print(f"Ez a szám {n}",end=' ')
    print("páros!") if parity(n) else print('páratlan!')


# 02-06. Függvény: Páros-páratlan - igaz/hamis
def paratlan_e():
    """
        Írj egy függvényt "paratlan_e" néven, amely igazat ad vissza ha a bejövő paraméter páratlan és hamisat ha páros.
    """


# 02-07. Függvény: Háromszoros
def haromszoros():
    """
        Írj egy függvényt "haromszoros" néven, amely visszaadja a bejövő szám háromszorosát.
    """


# 02-08. Függvény: Nagyobb dupla
def nagyobbdupla():
    """
        Írj függvényt "nagyobbDupla" néven, amely a két szám közül nagyobbnak adja vissza a dupláját.
    """


"""
03. Fájlkezelés
"""


# 03-01. Véletlen számok fájlba
def fileveletlen():
    """
        Generálj 50 egész számot és azokat írd ki egy szamok.txt fájlba. Minden szám külön sorba kerüljön.
    """


# 03-02. Páratlan számok fájlba
def paratlanfile():
    """
        Olvass be számokat addig amíg 0-át nem írnak be.
        Ha páratlan számot adtak meg, akkor azt írd ki egy fájlba (paratlan.txt), mindegyik számot külön sorba.
    """
