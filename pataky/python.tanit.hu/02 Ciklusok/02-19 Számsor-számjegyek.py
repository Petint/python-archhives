"""Adott az alábbi adatsor. Írjuk ki, hogy hány egyjegyű, hány kétjegyű és hány háromjegyű szám van benne."""
dataList = [210, 23, 124, 3, 5, 567, 56, 87, 9, 7, 3, 45, 2345, 678, 543, 24, 3, 567, 2, 1, 12, 48, 9, 12, 345, 64, 87, 84, 347, 56, 2, 3, 14, 7243, 578, 93, 432, 34, 567, 43, 234, 543, 467, 876, 510, 120, 123]
dataLengths = [0 for _ in range(5)]
for data in dataList:
    dataLengths[len(str(data))] += 1
print(f'A listában {dataLengths[1]} egyjegű, {dataLengths[2]} kétjegyű és {dataLengths[3]} háromjegyű szám van.')
