dataList = """Név\tÉletkor\tVáros
Agárdi Pál\t26\tBudapest
Pálosi Richárd\t23\tBudapest
Budai Máté\t19\tDebrecen
Karácsony Antal\t20\tBudapest
Román Sarolta\t24\tBudapest
Virág Bertalan\t22\tPécs
Varga Imre\t18\tBudapest
Tóth Sándor\t22\tDebrecen
Nagy Ibolya\t23\tPécs
Horváth Ferenc\t17\tBudapest
Balogh Edina\t26\tBudapest
Németh Kamilla\t19\tDebrecen
Fekete Géza\t18\tPécs
Kovács Péter\t27\tBudapest
Kiss Tibor\t20\tDebrecen
Szabó Erzsébet\t21\tBudapest
Szilágyi Ede\t18\tPécs
Aradi Márta\t27\tPécs
Piros Adél\t29\tDebrecen
Bíró Zsolt\t16\tBudapest
Szabados Attila\t25\tDebrecen
"""
debre_people = 0
for ppl in dataList.splitlines()[1:]:
    nev, kor, city = ppl.split('\t')
    # print(nev, kor, city)
    if city == 'Debrecen':
        debre_people += 1
print(f'{debre_people} Debreceni talalhato',)
