"""
01-14 Magánhangzók száma
Feladat leírás:
Olvass be egy szöveget és írd ki, hogy hány magánhangzó van benne. A kis és nagybetűk is számítanak.
"""

print("Megszámoljuk egy szövegben a magánhangzókat.")
vovs = 'aáeéiíoóöőuúüű'
du = input("Adj meg egy szöveget: ").lower()
n = 0
for i in du:
    if i in vovs:
        n += 1
print(f"A szövegben ({du}) {n} magánhangzó található.")
