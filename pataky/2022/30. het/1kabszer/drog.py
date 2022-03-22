path = 'Kabitoszer buncselekmenyek.txt'
illegal_file = open(path, "rt", encoding="utf-8")
print(f"Kiirjuk a \"{path}\" tartalmadol a 2015 utani buncselekmenyek szamat.")
illegal_drugs = illegal_file.read().splitlines()
illegal_file.close()
illegal_data = [illegal_drugs[i].split("\t") for i in range(len(illegal_drugs))]

