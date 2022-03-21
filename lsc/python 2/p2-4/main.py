from random import randint as ndom
import matplotlib.pyplot as plt
import numpy as np
# 1. feladat yield return

"""def NSzCs():
    k = 1
    while True:
        yield k * k
        k += 1

        
for num in NSzCs():
    print(num)
    if num > 100:
        break"""

# 2. only print even numbers

def OpEn(teszt):
    for i in teszt:
        if i % 2 == 0:
            yield i


"""testlist = []
while len(testlist) < 20:
    value = ndom(1,100)
    if value not in testlist:
        testlist.append(value)

print(f"Eredeti lista: {testlist}")
print("lista páros elemei:", end="")
for j in OpEn(testlist):
    print(j, end=' ')
print('\n')
"""

# 3. bevásárlás szimulátor

items = ["Sárgarépa", "Répakonzerv", "Répakenyér", "Répavíz", "Répakifli", "Répalekvár", "Répasárga NoHab", "Répasárga festék",
         "Fehérrépa"]
prices = [10, 30, 40, 100, 35, 60, 9420, 300, 20]
basket = []
EeePeeCee = []    #itemprice

def WLABzxmpzreet():
    itemCount = int(input("Mennyi terméket akarsz venni?\n: "))
    for i in range(itemCount):
        rng = ndom(0, len(items) - 1)
        basket.append(items[rng])
        EeePeeCee.append(prices[rng])
        print(f"{basket[i]} --- {EeePeeCee[i]}Ͳ")
        sum = 0
        minx = maxx = EeePeeCee[0]
    for ggg in EeePeeCee:
        sum += ggg
        if ggg > maxx:
            maxx = ggg
        if ggg < minx:
            minx = ggg
    print(f"Összesen: {sum}Ͳ\nLegkisebb: {minx}Ͳ\nLegnagyobb: {maxx}Ͳ")
WLABzxmpzreet()
# tanár ímél --- darabos2001@gmail.com ---