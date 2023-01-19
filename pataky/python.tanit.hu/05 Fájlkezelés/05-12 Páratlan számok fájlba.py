"""
05-12 Páratlan számok fájlba
Feladat leírás:
Olvass be egész számokat addig amíg 0-át nem írnak be.
Ha páratlan számot adtak meg, akkor azt írd ki a "paratlan.txt" fájlba, mindegyik számot külön sorba.
Ha nem egész számot adnak meg, vagy nem páratlan a szám, akkor azt hagyjuk figyelmen kívül és kérjük a következőt.
"""

run = True
odd_file = open('paratlan.txt', 'wt')
while run:
    try:
        du = int(input('Enter a number: '))
    except ValueError:
        pass
    else:
        if du == 0:
            run = False
        elif du % 2:
            odd_file.write(str(du) + '\n')
        else:
            pass
odd_file.close()
