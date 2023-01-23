"""
A mellékelt forráskódot egészítsd ki, hogy a 'data' listáról írja ki az alábbi információkat a mintának megfelelően.
Az adatok a fájlban fejléc nélkül szerepelnek az alábbi minta szerint:
Lengyel Elizabet;1979-04-15;Szolnok;Pék
Dudás Bence;2001-11-08;Debrecen;Üzletkötő
Halász Ferenc;1988-12-26;Érd;Raktárkezelő
Antal Viktória;1982-02-28;Miskolc;Óvónő

Minden beolvasott sor a 'data' listában a pontosvesszők mentén al-listában van tárolva úgy, hogy egy sor a fájlból a 'data' egy eleme lett. Ezek ez elemek al-listák, ahol az első elem a név, a második elem a születési dátum, a harmadik a lakhely, negyedik pedig a foglalkozás.

Írassuk ki az alábbi adatokat:
- hány név szerepel a listában
- ki a legfiatalabb, mikor született és hol lakik
- ki a legidősebb, mikor született és mi a foglalkozása
- hány budapesti szerepel a listában
- hány szolnoki pék szerepel a listában

A program akkor is helyesen működjön, ha más a beolvasott fájl tartalma, de a struktúrája azonos.
"""
# Tájékoztatjuk a felhasználót, hogy hogyan működik a program
print('Egy fájlból beolvasott lista elemeiről írunk ki információkat.')
# A beolvasandó fájl neve
fileName = 'data.txt'

# Megnyitjuk a text (t) fájlt olvasásra (r)
file = open(fileName, 'tr', encoding="utf-8")
# Létrehozunk egy üres listát
data = []
# Indítunk egy ciklust amely végigmegy a fájl sorain
for row in file.read().splitlines():
    # Ha üres a sor, akkor továbblépünk
    if row == '':
        continue
    # Elkészítjük az al-listát, pontosvessző mentén tagolva az adatokat
    newItem = row.split(';')
    # Felvesszük a 'data' listába az új elemet, vagyis az al-listát
    data.append(newItem)

# Lezárjuk a fájlt
file.close()


def getmin(_input: 'list[list]'):
    mini = min(_input)
    print(f"A legfiatalabb: {mini[0]}, született: {mini[1]}, Lakhelye: {mini[2]}")


def getmax(_input: 'list[list]'):
    maxi = max(_input)
    print(f"A legidősebb: {maxi[0]}, született: {maxi[1]}, Lakhelye: {maxi[2]}")

def budapest(dta: 'list[list]'):
    cnt = 0
    for x in dta:
        cnt += x.count("Budapest")
    print(f"A budapestiek száma: {cnt}")


def szolnok(dta: 'list[list]'):
    pekek = 0
    for x in dta:
        if x[2] == 'Szolnok' and x[3] == 'Pék':
            pekek += 1
    print(f"A szolnoki pékek száma: {pekek}")


print(f"A lista elemeinek száma: {len(data)}")
getmin(data)
getmax(data)
budapest(data)
szolnok(data)

