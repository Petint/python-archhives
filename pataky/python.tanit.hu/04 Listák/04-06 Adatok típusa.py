"""
Írasd ki egyesével, külön sorokba az alábbi lista (dataList) elemeit és azt, hogy az elemek milyen típusúak:
"""
dataList = [12, 34.5, True, 'abc', (2, 3), {5, 6, 7}, ['a', 3, 4], False, {'name':'Alfa', 'age':15}, None]
print('Előre megadott lista értékeit és típusait írjuk ki.')
for data in dataList:
    print(data, '-', type(data).__name__)