dataList = """Név,Életkor,Város
Varga Imre,18,Budapest
Tóth Sándor,22,Debrecen
Nagy Ibolya,23,Pécs
Horváth Ferenc,17,Budapest
Balogh Edina,26,Budapest
Németh Kamilla,19,Debrecen
Fekete Géza,18,Pécs
Kovács Péter,27,Budapest
Kiss Tibor,20,Debrecen
Szabó Erzsébet,21,Budapest
Szilágyi Ede,18,Pécs
Agárdi Pál,26,Budapest
Pálosi Richárd,23,Budapest
Budai Máté,19,Debrecen
Karácsony Antal,20,Budapest
Aradi Márta,27,Pécs
Piros Adél,29,Debrecen
Bíró Zsolt,16,Budapest
Szabados Attila,25,Debrecen
Román Sarolta,24,Budapest
Virág Bertalan,22,Pécs
"""

"""Ebből a listából programmal keresd ki a legfiatalabb résztvevőt és írd ki a nevét, életkorát és városát.
A program akkor is helyesen működjön, ha az adatlista módosul."""

oldest = ('', 99, '')
pest = ('', -1)
for line in dataList.splitlines()[1:]:
    person = line.split(',')
    if int(person[1]) < int(oldest[1]):
        oldest = person
    if int(person[1]) > pest[1] and person[2] == 'Budapest':
        pest = person[0], int(person[1])
print(oldest)
print(pest)
