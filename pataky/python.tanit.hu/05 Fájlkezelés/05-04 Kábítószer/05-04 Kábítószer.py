"""
A 'Kábítószeres bűncselekmények.txt' utf-8 kódolású szövegfájl tartalmazza a 2009 és 2020 között Magyarországon elkövetett kábítószeres bűncselekmények számát.
Keresd meg algoritmussal és írd ki a konzolra a 2015 utáni években elkövetett bűncselekmények számát.
A program akkor is jól működjön, ha frissítik az adatfájlt a legutóbbi évek adataival.
"""

path = 'Kabitoszer buncselekmenyek.txt'
illegal_file = open(path, "rt", encoding="utf-8")
print(f"Kiirjuk a \"{path}\" tartalmadol a 2015 utani buncselekmenyek szamat.")
illegal_drugs = illegal_file.read().splitlines()
illegal_file.close()
illegal_data = [illegal_drugs[i].split("\t") for i in range(len(illegal_drugs))]

lots_of_drugs = 0
for year in illegal_data:
    try:
        if int(year[0]) >= 2016:
            print(f"{year[0]} - {year[1]}")
        if int(year[1]) > lots_of_drugs:
            year_of_drugs, lots_of_drugs = int(year[0]), int(year[1])
    except ValueError:
        pass

print(f"{year_of_drugs} évben követték el a legtöbb kábítószeres bűncselekményt : {lots_of_drugs}")
