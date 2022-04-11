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


# def legfiatalabb(dta: 'list[list]'):
#     mini = dta[0][1]
#     for x in dta:
#         if x[1] < mini:
#             mini = x[1]
#     # x = dta.index(mini)
# 
#     return mini


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

