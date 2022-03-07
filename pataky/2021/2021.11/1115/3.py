# olvass be egy söveget és írd ki a mássalhangók számát
mgh = "wrtzipsdfghjklyxcvbnm"
teXt = input("Adj meg egy szöveget > ").lower()
szama = 0
for breif in teXt:
    if breif in mgh:
        szama+=1
print(f"Az adott szövegben {szama} Mássalhangó található.")
if szama == 0:
    print("Tehát nincseen! >:)")