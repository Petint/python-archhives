szamok = []
for x in range(10):
    szamok.append(float(input("Adj meg egy számot\n>")))
paros = 0
paratlan = 0
pozitiv = 0
negativ = 0
nulla = 0
for i in szamok:
    if i > 0:
        pozitiv += 1
    elif i < 0:
        negativ += 1
    else:
        nulla += 1
    if i % 2 == 0:
        paros += 1
    else:
        paratlan += 1
print(f"Páros: {paros}\nPáratlan: {paratlan}\nPozitív: {pozitiv}\nNegatív: {negativ}\nNulla: {nulla}\n")

# 2. feladat

nums = [1, 2, 3, 4, 5, 4, 4, 2, 1, 6, 1]
print(str(nums))
new_nums = []
Skipped_nums = 0
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
    else:
        Skipped_nums += 1
print(new_nums)
print(Skipped_nums)

# 3 & Knuckles. Feladat

list = [1, 2, 3, 4]
list.extend("Hello, világ!")
print(list)
list.extend([1, 2, 3, "LooL ScoocS TáT"])
print(list)

# 4. feladat -- egész számok keresése
every_list_be_like = [321, "rs-232", True, 12, 3.141, 4, 5, "allat.py", "0", False, 3.1, 4, list]
intigers_list = []
for f in every_list_be_like:
    if type(f) == int:
        intigers_list.append(f)
print(intigers_list)

# 5. feladat - terjedelem
from random import randint

rng = []
for x in range(100):
    rng.append(randint(0, 100))
minx = min(rng)
maxx = max(rng)
rangex = maxx - minx
print(f"Legkisebb: {minx}\nLegnagyobb: {maxx}\nTerjedelem: {rangex}")

# 6. FeleF
print(rng)
index = 0
largest_number = rng[0]
while index < len(rng):
    if largest_number < rng[index]:
        largest_number = index
    index += 1
print(largest_number)
index = 0

second_largerst = rng[0]
while index < len(rng):
    if second_largerst < rng[index] and largest_number != rng[index]:
        second_largerst = index
    index += 1
    print(second_largerst)
