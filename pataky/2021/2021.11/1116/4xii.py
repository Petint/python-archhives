fgj = int(input("Aggy eggy szám-t! "))
osztok = 0
for g in range(1,fgj+1):
    if fgj % g == 0:
        osztok+=1
print("Prim") if osztok == 2 else print("nem prím")
