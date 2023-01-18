"""
Olvass be egy egész számot. Írd ki ha nagyobb tíznél: "Nagy", különben azt, hogy "Kicsi".
Biztosra vehetjük, hogy egész számot adunk meg.
"""
print('Egy beolvasott számról állapítjuk meg, hogy kicsi-e vagy nagy. Akkor nagy, ha nagyobb 10-nél.')
number = int(input('adj meg egy egész számot: '))
if number > 10:
    print('Nagy')
else:
    print('kicsi')
