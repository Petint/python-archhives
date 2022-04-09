import feladatok


def leker(du: str):
    if du == "01-01":
        feladatok.Szovegszam(input("Adj meg egy számot: "))
    elif du == "01-02":
        feladatok.Szamoktipusa(input("Adj meg egy számot: "))
    elif du == "01-02b":
        feladatok.Szamoktipusb()
    elif du == "01-03":
        feladatok.Nagyobb(int(input("adj meg egy számot: ")),
                          int(input("adj meg egy számot: ")))
    elif du == "01-04":
        feladatok.Parosparatlan(input("Adj meg egy számot: "))
    elif du == "01-05":
        feladatok.Soveghoszz()
    elif du == "01-06":
        feladatok.Nagyobb10(int(input("Adj meg egy számot: ")))
    elif du == "01-07":
        print(feladatok.Dupla())
    elif du == "01-08":
        feladatok.Betukereso()
    elif du == "01-09":
        print("A legkisebb szám:", feladatok.Legkisebb(int(input("Hány számot akarsz megadni? "))))
    elif du == "01-10":
        feladatok.Kitalalosdi()
    elif du == "01-11":
        feladatok.Szamsor()
    elif du == "01-12":
        feladatok.Veletlenzamsor()
    elif du == "01-13":
        feladatok.lista_es_oszthatosag()
    elif du == "01-14":
        feladatok.maganhanguok(input("Add meg egy szöveget: "))
    elif du == "01-15":
        feladatok.szam_tip()
    elif du == "01-16":
        feladatok.primszam()
    elif du == "01-17":
        feladatok.beleptetes()
    elif du == "01-18":
        feladatok.szamsor()
    elif du == "01-19":
        feladatok.abcsor()
    elif du == "01-20":
        feladatok.nevsor()
    elif du == "01-21":
        feladatok.szovegsorozat()
    elif du == "01-22":
        feladatok.szamokfele()
    elif du == "01-23":
        nums = feladatok.veletlenszaz()
        feladatok.min_max_atlag(nums)
    elif du == "01-24":
        feladatok.kiertekeles(feladatok.veletlenszaz())
    elif du == "01-25":
        feladatok.veletlenatlag(input("Adj meg egy számot: "))
    elif du == "01-26":
        feladatok.szamolas()
    elif du == "02-01":
        print(feladatok.parity(int(input("Adj meg egy számot: "))))
    elif du == "02-02":
        n1, n2 = input("Adj meg egy számot: "), input("Adj meg egy számot: ")
        try:
            print("A két szám szorzata:",feladatok.szorzat(n1, n2))
        except ValueError:
            print("Nem számot adtál meg.")
    elif du == "02-03":         # nice
        print("A kisebb szám duplája:", feladatok.kisebb_dupla(int(input("Adj meg egy számot: ")), int(input("Adj meg egy számot: "))))
    elif du == "02-04":
        try:
            print("Magánhangzó") if feladatok.maganhangzo(input("Adj meg egy betűt: ")) else print("Mássalhangzó")
        except ValueError:
            print("Nem egy betűt adtál meg!")
    elif du == "02-05":
        feladatok.paros_paratlan(int(input('Adj meg egy számot: ')))
    elif du == "02-06":
        print("02-06")
    elif du == "02-07":
        print("02-07")
    elif du == "02-08":
        print("02-08")
    elif du.lower() in "exitexteyreytxt":
        exit()
    else:
        print("A feladat nem található.")


if __name__ == '__main__':
    while True:
        leker(input("Hányas feladat? "))
