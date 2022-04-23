puzzle = "alma"  # Kitalálandó szó
megoldas = ""  # A játékos megoldása
for x in puzzle:  # végigmegy a kitalálandó szavat és kitölti csillagokkal
    if x == " ":
        megoldas += " "
    else:
        megoldas += "*"
correct = []  # Helyes betük listája
incorrect = []  # Helytelen betük
lifes = 10  # Probálkozások száma


def Elet():
    global lifes
    lifes -= 1
    print(f"{lifes} élet van hátra.")


while puzzle != megoldas and lifes > 0:  # Fő játék ciklus
    print(megoldas)  # Ki írja a jelenlegi tippet
    print(correct)
    print(incorrect)
    tipp = input("Tippelj egy betűt:\n> ")
    if len(tipp) == len(puzzle):  # Ha a karakterek száma ugyan annyi
        temp = megoldas  # Ideglenesen eltárolja a megoldást, hogy később visszaálithassa
        megoldas = tipp  # A tippet átrakja a megoldásba, hiszen a program azzal ellenőrzi
        print("Megpróbáltál tippelni")
        if megoldas == puzzle:
            print("Helyes Válasz")
        else:
            print("Ez helytelen. (-1 élet.)")
            megoldas = temp
            Elet()
    else:
        talalat = False
        for b in range(len(puzzle)):
            if b == puzzle[b]:
                megoldas_lista = list(megoldas)
                megoldas_lista[b] = tipp
                megoldas = "".join(megoldas_lista)
                talalat = True
        if not talalat:
            print("Ilyen betű nincsen. (-1 Élet.)")
            incorrect.append(tipp)
            Elet()
        else:
            correct.append(tipp)  # megnézi hogy vannak-e helyes betűk
if lifes > 0:
    print("Nyertél!")
else:
    print("Vesztettél")
