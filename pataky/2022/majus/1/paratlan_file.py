"""
05-12 Páratlan számok fájlba
Feladat leírás:
Olvass be egész számokat addig amíg 0-át nem írnak be.
Ha páratlan számot adtak meg, akkor azt írd ki a "paratlan.txt" fájlba, mindegyik számot külön sorba.
Ha nem egész számot adnak meg, vagy nem páratlan a szám, akkor azt hagyjuk figyelmen kívül és kérjük a következőt.
"""
print('Adj meg egész számokat. Közölük a páratlanokat kiírjuk a "paratlan.txt" fájlba.')
paratfile = open("paratlan.txt", 'w')
du = -1
while du != 0:
    du = int(input("Adj meg egy egész számot:   "))
    if du % 2:
        paratfile.write(str(du)+'\n')
print('A file elkészült.')
paratfile.close
