import math
# 1. feladat: metódusok létrehozása
"""def kiiras():
    print("Hello, world!")
kiiras()"""

# 2. feladat: prímszám eldöntő
"""nums = []
for num in range(0,100):
    Test(num)
def Test(szam):
    prime = True
    for x in range(2,szam):
        if szam % x == 0:
          prime = False
    if prime == True:
        nums.append(szam)
        print(szam, "Prím szám")
    else:
        print(szam,"Nem prím")"""

# 3. feladat: paraméterek

"""almaa = "..........................."

def Formatter(parameter):
    for x in parameter:
        print(x, end="\t")
Formatter(almaa)"""

# 4. feladat: prímszám eldöntő bemenettel
"""
nums = []
def TestParameter(szam):
    prime = True
    for x in range(2,szam):
        if szam % x == 0:
          prime = False
    if prime == True:
        nums.append(szam)
        print(szam, "Prím szám")
    else:
        print(szam,"Nem prím")
for num in range(0,10000):
    TestParameter(num)
print(nums)
"""
# 5. feladat: háromszögek
"""
a = int(input("A háromszög egyik oldala\n> "))
b = int(input("A háromszög második oldala\n> "))
c = int(input("A háromszög harmadik oldala\n> "))


def dszhsz(a1, b1, c1):
    if (math.sqrt(a1) + math.sqrt(b1) == math.sqrt(c1)) \
     or (math.sqrt(b1) + math.sqrt(c1) == math.sqrt(a1)) \
     or (math.sqrt(c1) + math.sqrt(a1) == math.sqrt(b1)):
        print("Yes.")
    else:
        print("N0.")

dszhsz(a,b,c)
"""

# 6. feladat: Abs. érték

"""
def absval(numin):
    return math.fabs(numin)


print(absval(int(input("Írj egy számot\n> "))))
"""

# 7. feladat: Üzemanyagszámítás
# Five miles out
"""
def lipkm_to_MPG(liter):
    gallon = liter / 3.8
    miles = 100 / 1.6
    return miles/gallon


def MPG_to_lipkm(miles):
    liter = 3.8
    kms = 1.6 * miles
    return 100 * liter / kms


print(lipkm_to_MPG(100))
print(MPG_to_lipkm(2.375))
"""

# 7. feladat: sokszoros visszatértés


def ExitFuncton():
    for i in range(1, 10):
        if i > 5:
            return "run is over"
        print(i)


print(ExitFuncton())
