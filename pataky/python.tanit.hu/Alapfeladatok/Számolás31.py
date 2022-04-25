"""
01-31 Számolás
Feladat leírás:
Kérjünk be a felhasználótól két darab kétjegyű egész számot.
Biztosak lehetünk benne, hogy azt ad meg, ezért nem kell ellenőrizni.
Utána írjuk ki a két számmal elvégzett műveleteket és azok eredményét a minta szerint.
"""
print("Két megadott kétjegyű számmal végzünk el műveleteket.")
du = int(input("Adj meg egy számot: ")), int(input("Adj meg egy számot: "))
results = f"{du[0]} + {du[1]} = {du[0]+du[1]}\n"
results += f"{du[0]} - {du[1]} = {du[0]-du[1]}\n"
results += f"{du[0]} * {du[1]} = {du[0]*du[1]}\n"
try:
    results += f"{du[0]} / {du[1]} = {du[0]/du[1]}, Két tizedrsre kerekírve: {round(du[0]/du[1], 2)}\n"
except ZeroDivisionError:
    results += "Nullával nem lehet osztani."
print(results)
