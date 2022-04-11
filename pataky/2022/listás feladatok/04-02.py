# Beolvassuk a véletlen számokat generáló modulból az egész szám generáló függvényt
from random import randint 

itemCount = 5 # A lista elemeinek száma
data = [] # Létrehozunk egy üres listát
# Indítunk egy ciklust a véletlen számok létrehozására
for i in range(itemCount):
    newItem = randint(1, 20) # Generálunk egy új véletlen egész számot
    data.append(newItem) # Felvesszük a listába az új elemet


print('Egy véletlenszerű számokból álló lista elemiről írunk ki információkat.') # Tájékoztatjuk a felhasználót, hogy hogyan működik a program
print("A 'data' lista tartalma: ", data) # Kiírjuk a lista tartalmát
# Kiírjuk a kért információkat
print(f"""
Egy előre meghatárorott lista elemeiről írunk ki információkat.
A lista {len(data)} elemet tartalmaz.
A lista legnagyobb értéke: {max(data)}
A lista első eleme: {data[0]}
A lista utolsó eleme: {data[-2]}
A lista első és utolsó előtti elemének szorzata: {data[0] * data[-2]}
A lista második és harmadik elemének a külöbmsége: {data[1] - data[2]}
A lista legkisebb éretékének a duplája: {min(data) * 2}
A lista elemeinek az összege: {sum(data)}
A lista elemeinek az átlaga: {sum(data) / len(data)}
""")