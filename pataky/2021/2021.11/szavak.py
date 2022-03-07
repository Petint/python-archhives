# 2021.11.02 10a pbq szavak.py
# kérjünk be ket szót
# Írjuk ki mejik hosszabb
# Ha egyforma azt írjuk.

words = [0,1]
for w in words:
    words[w] = input("Adj egy szavat\n:").__len__()

if words[0] > words[1]:
    print("Az első hasszabb.")
elif words[1] > words[0]:
    print("A második hosszabb")
else:
    print("A két szó egyforma hosszú.")
