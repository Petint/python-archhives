def szam(_txt:str):
    """Olvassunk be egy számot és írjuk ki hogy szám-e"""

    if _txt.isnumeric():
        return "Szám"
    else:
        return "Nem szám"


def legkisebb(_num:int):
    """Kérd be hogy hány számot akar  megadni a DU
    majd annyi számot kérünk be és kiírjuk a legkisebbet."""

    nums = [int(input("Adj meg egy számot: ")) for x in range(_num)]

    min = nums[0]
    for x in nums:
        if x < min:
            min = x
    
    return min


def kitalalosdi():
    """A DU tippeljen meg egy véletlen egész számot
    amely 1-5 között van, Addig tippelhet ameddig nem találja el."""
    
    from random import randint
    _secret = randint(1,5)
    run = True
    while run:
        _du = int(input("Adj meg egy számot (1-5): "))
        if _du == _secret:
            print("Ez volt a helyes szám.")
            run = False


print(szam(input("Adj meg egy számot: ")))
print(legkisebb(int(input("Add meg hogy hány számot akarsz beadni: "))))
kitalalosdi()
