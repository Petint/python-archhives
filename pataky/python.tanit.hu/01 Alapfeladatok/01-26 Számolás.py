"""
01-26 Számolás
Feladat leírás:
Kérjünk be két egész számot.
Ha nem egész számot adtak meg, akkor írjuk ki, hogy ez nem egész szám.
Különben írjuk ki a két szám összegét, különbségét, szorzatát és hányadosát.
A hányadost csak akkor írjuk ki, ha az osztó nem nulla.
"""
print("Kiírjuk két szám összegét, különbségét, szorzatát és hányadosát.")
dear_user = ()
while len(dear_user) < 2:
    try:
        dear_user = int(input("Adj meg egy számot: ")), int(input("Adj meg egy számot: "))
    except ValueError:
        print("Nem számot adtál meg")
results = f"{dear_user[0]} + {dear_user[1]} = {dear_user[0]+dear_user[1]}\n"
results += f"{dear_user[0]} - {dear_user[1]} = {dear_user[0]-dear_user[1]}\n"
results += f"{dear_user[0]} * {dear_user[1]} = {dear_user[0]*dear_user[1]}\n"
try:
    results += f"{dear_user[0]} / {dear_user[1]} = {dear_user[0]/dear_user[1]}\n"
except ZeroDivisionError:
    results += "Nullával nem lehet osztani."
print(results)
