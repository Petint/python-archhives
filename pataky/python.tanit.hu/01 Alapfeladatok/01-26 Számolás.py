"""
01-26 Számolás
Feladat leírás:
Kérjünk be két egész számot.
Ha nem egész számot adtak meg, akkor írjuk ki, hogy ez nem egész szám.
Különben írjuk ki a két szám összegét, különbségét, szorzatát és hányadosát.
A hányadost csak akkor írjuk ki, ha az osztó nem nulla.
"""
print("Kiírjuk két szám összegét, különbségét, szorzatát és hányadosát.")
du = ()
while len(du) < 2:
    try:
        du = int(input("Adj meg egy számot: ")), int(input("Adj meg egy számot: "))
    except ValueError:
        print("Nem számot adtál meg")
# print(du)
results = f"{du[0]} + {du[1]} = {du[0]+du[1]}\n"
results += f"{du[0]} - {du[1]} = {du[0]-du[1]}\n"
results += f"{du[0]} * {du[1]} = {du[0]*du[1]}\n"
try:
    results += f"{du[0]} / {du[1]} = {du[0]/du[1]}\n"
except ZeroDivisionError:
    results += "Nullával nem lehet osztani."
print(results)
