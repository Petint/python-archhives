
def koszontes(nev):
    print(f"Szia {nev}!")


def paros(num):
    print(f"Ez a szám ({num}) páros.") if num % 2 == 0 else print(f"Ez a szám ({num}) Páratlan.")


tripla = lambda x : x*3


def nagydupla(x, y):
    nagyxbb = max(x,y)
    return nagyxbb * 2


def szamkero():
    try:
        num = int(input("Adj egy számot: "))
    except:
        raise ValueError("Nem számot adtál meg!")
    return num
    # paros(num)

def nevek():
    # Kérj be öt nevet és ír4d ki a névsorban a leg elsőt!
    names = []
    for x in range(5):
        names.append(input("Adj öt nevet! ").lower())
    for name in names:
        if name < names[0]:
            names[0] = name
    print(names[0])

def ge():
    from random import randint
    joe = randint(1,3)
    _num = szamkero()
    if _num == joe:
        print(f"Eltaláltad, a helyes szám a(z) {joe} volt!")
    else:
        print(f"Nem találtad el! a helyes szám a(z) {joe} volt.")

"""
koszontes("uram")
koszontes("Lajos")
koszontes("Joe")
paros(10)
paros(347)
print(tripla(333))
print(nagydupla(111,333))
szamkero()
nevek()
"""
ge()
