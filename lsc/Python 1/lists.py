import winsound

nevek = ["Józsi", "Géza", "Pista", "Anna"]
print(type(nevek))
print(nevek)
print(nevek[0])

print("2. feladat")
print(len(nevek))
print(nevek.__len__())

print("3. Feladat")
print(nevek[0])
print(nevek[2])
print(nevek[3])

print("4. Feladat")
for x in nevek:
    print(x)

print("5. feladat")
be = int(input("Hányadik elem?\n>")) - 1
if be < len(nevek):
    print(nevek[be])
else:
    print("Ilyen nincsen.")
    winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)

print("6. feladat.")
szamok = []
for x in range(0, 51):
    szamok.append(x)
print(szamok)

print("7. feladat")
paratlan = []
paros = []
for x in szamok:
    if x % 2 == 1:
        paratlan.append(x)
    else:
        paros.append(x)
print(paratlan)
print(paros)

print("8. felafdat")
losta1 = [1, 5, 12, 52, 56]
losta2 = [7, 12, 21, 44, 75]
for x in losta1:
    temp = losta1[x]
    losta1 = losta2[x]
    losta2[x] = temp
print("losta1: ", losta1)
print("losta2: ", losta2)
