# raketa.py pbq 20211103
"""
Hány óra mulva indul a rakéta?
Van halasztás?
Mennyi halasztás?

"""
print("Hány óra mulva indul a rakéta?",end=" :")
hoursToGo = int(input())
halasztas = 0
# print(hoursToGo)
for hours in range(hoursToGo,0,-1):
    print(hours)
    print("Szia uram! Jó halsztás nem kell? [I/N] ",end=" : ")
    _du = input().lower()
    if _du == "i":
        halasztas +=1

print(f"A visszaszámlálástól kezdve {hoursToGo + halasztas} óra mulva indult.")

