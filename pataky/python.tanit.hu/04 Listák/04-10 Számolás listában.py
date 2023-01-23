"""
Ebből a listából programmal számold meg hány 20 év feletti budapesti van.
A program akkor is helyesen működjön, ha az adatlista módosul.
"""
dataList = """Név*Életkor*Város
Nagy Ibolya*23*Pécs
Horváth Ferenc*17*Budapest
Agárdi Pál*26*Budapest
Pálosi Richárd*23*Budapest
Budai Máté*19*Debrecen
Karácsony Antal*20*Budapest
Román Sarolta*24*Budapest
Virág Bertalan*22*Pécs
Varga Imre*18*Budapest
Kovács Péter*27*Budapest
Kiss Tibor*20*Debrecen
Szabó Erzsébet*21*Budapest
Szilágyi Ede*18*Pécs
Aradi Márta*27*Pécs
Piros Adél*29*Debrecen
Bíró Zsolt*16*Budapest
Szabados Attila*25*Debrecen
Tóth Sándor*22*Debrecen
Balogh Edina*26*Budapest
Németh Kamilla*19*Debrecen
Fekete Géza*18*Pécs
"""

dataList = dataList.splitlines()
dataList = (data.split('*') for data in dataList)
next(dataList)
# [print(data) for data in dataList]
valid_people = 0
for name, age, city in dataList:
    if age > 20 and city == 'Budapest':
        valid_people += 1
print(f'Összesen {valid_people} Budapesti, 20 év feletti van a listában.')
