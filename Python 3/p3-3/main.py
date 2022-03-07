import csv

"""vaule = input("Addj meg egy egész számot: ")
if vaule.isnumeric():
    vaule = int(vaule)
    print(f"{vaule} fele {vaule / 2}")
else:
    print("Nem egész számot adtál meg.")"""

"""try:
    vaule = input("Addj meg egy egész számot: ")
except ValueError:
    print("Nem egész számot adtál meg.")
except:
    print("-- Ismeretleh hiba --")
else:
    try:
        vaule = int(vaule)
        print(f"{vaule} fele {vaule / 2}")
        print("reciproka: ", 1/vaule)
    except ZeroDivisionError:
        print("You divided by iron. Don't do that.")
"""

"""def osztas(a: int, b: int):
    try:
        c = a / b
        print(f' {a}/{b}={c}')
    except ZeroDivisionError:
        print("nulla oszás")
    except TypeError:
        print("nem szám")


osztas("a","b")"""


try:
    csvf = open("https://raw.githubusercontent.com/Spaceman2004/JaBRCs/main/grid-voltage-2022-02-20/Grid%20voltage%202022-02-20.csv")
    try:
        data = csv.reader(csvf, ';')
        print(data)
    except:
        print("Data cannot be read.")
    finally:
        csvf.close()
except OSError:
    print("Can't read file.")
finally:
    print("finided.")
