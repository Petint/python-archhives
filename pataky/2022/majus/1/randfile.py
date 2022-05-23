"""
Generálj 50 véletlen pozitív egész háromjegyű számot és azokat írd ki egy "szamok.txt" fájlba. Minden szám külön sorba kerüljön.
"""
from random import randint
rf = open("szamok.txt","w",encoding="utf-8")
rn = [str(randint(0, 100))+'\n' for _ in range(50)]
rf.writelines(rn)
rf.close()
