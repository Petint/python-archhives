# adozas.py pbq 10a 20211106
from random import randrange as randy
from numpy import average as avrg
from numpy import max


def taxcalc(income):
    if income < 500:
        tax = income * 0.12 - 1
        if tax < 0:
           tax = 0.0
    else:
        tax = 149 + (income - 500)
    return round(tax,0)


incommatrix = [
    [100, 2000, 24315, 424],
    [69, 420, 486, 6502],
    [8088, 80486, 1401, 68000],
    [747, 634, 11, 69.69]
]

taxxez = []

for mone in incommatrix:
    for per_person in mone:
        tax = taxcalc(per_person)
        taxxez.append(tax)

for this in range(len(taxxez)):
    print(f"tax of person {hex(this)} :: {taxxez[this]}")

# list = [expression for item in collection]


def lch():
    lils0ne = []
    for i in range(4, 75):
        lils0ne.append(i)
    print(lils0ne)
    print("")
    list2 = [x for x in range(4, 76)]
    for x in list2: print(hex(x), end=" ")
    print("")


def even():
    liste = [hex(x) for x in range(101) if x % 2 == 0]
    print(liste)


def god():
    next_level = []
    next_level = [[i for i in range(10)] for j in range(10)]
    return next_level


def maxxit():
    maxxtrixx = [[i ** 4 + j for i in range(10)] for j in range(10)]
    return maxxtrixx


def maxtemp():
    temps = [[randy(-5, 32) for j in range(24)] for i in range(31)]
    dyly_avrg = []
    for day in temps: # nice
        dyly_avrg.append(avrg(day))
    maxday = 0
    maxx = dyly_avrg[0]

    return maxday



"""def average(day):
    sm = 0
    for hour in day:
        sm += hour
    return sm / len(day)"""


lch()
print("\n")
even()
print("")
# print(god())
for x in god(): print(x)
print("")
for x in maxxit(): print(x)
print("")
print(maxtemp())




