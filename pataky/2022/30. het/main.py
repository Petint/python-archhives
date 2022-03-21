"""File handling"""

# 05-01
import os.path
from random import randint

"""
Olvasd be a 'magyar-koltok-irok.txt' utf-8 kódolású szövegfájl tartalmát és írd azt ki a konzolra.
"""

path = "koltok.txt"
koltok_file = open(path, 'rt', encoding="utf-8")
koltok_file_data = koltok_file.read()
koltok_file.close()
print(koltok_file_data)

"""
05-02
Olvasd be a 'magyar-koltok-irok.txt' utf-8 kódolású szövegfájl tartalmát és írd ki a konzolra a költőket."""
koltok = koltok_file_data.splitlines()
del koltok_file_data
# print(koltok)
for k in koltok:
    if 'költő' in k.lower():
        print(k)

"""
05-11 Véletlen számok fájlba
Feladat leírás:
Generálj 50 véletlen pozitív egész háromjegyű számot és azokat írd ki egy "szamok.txt" fájlba. 
Minden szám külön sorba kerüljön.
"""
random_list = [randint(100, 999) for _ in range(50)]
numbers = open(os.path.join('szamok.txt'), 'wt')
for n in random_list:
    numbers.write(str(n)+'\n')
numbers.close()

"""
05-12 Páratlan számok fájlba
Feladat leírás:
Olvass be egész számokat addig amíg 0-át nem írnak be.
Ha páratlan számot adtak meg, akkor azt írd ki a "paratlan.txt" fájlba, mindegyik számot külön sorba.
Ha nem egész számot adnak meg, vagy nem páratlan a szám, akkor azt hagyjuk figyelmen kívül és kérjük a következőt.
"""

