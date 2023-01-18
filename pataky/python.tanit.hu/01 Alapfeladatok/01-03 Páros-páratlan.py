"""
Olvassunk be egy egész számot. Ha nem egész szám, akkor írjuk ki, hogy "Nem egész szám", különben írjuk ki, hogy páros-e vagy páratlan.
"""
print('Egy belolvasott egész számról állapítjuk meg, hogy páros-e vagy páratlan.')
number = int(input('adj meg egy egész számot: '))
if number % 2:
    print('Páratlan számot adtál meg.')
else:
    print('Páros számot adtál meg.')
