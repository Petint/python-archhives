"""
Adott az alábbi lista:
data = [3, 45, 6, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98]
A mintának megfelelő módon írjuk ki:
- hány elem van a listában
- a lista első elemét
- a lista utolsó elemét
- a lista harmadik és ötödik elemének az összegét
- a lista legkisebb értékét
- a lista legnagyobb értékét
- a lista elemeinek az összegét
- a lista elemeinek az átlagát
Akkor is helyesen működjön a program, ha módosítjuk a listát!
"""

data = [3, 45, 6, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98]

print(f"""
Egy előre meghatárorott lista elemeiről írunk ki információkat.
A lista {len(data)} elemet tartalmaz.
A lista első eleme: {data[0]}
A lista utolsó eleme: {data[-1]}
A lista harmadik és ötödik elemének összege: {data[2] + data[4]}
A lista legkisebb éretéke: {min(data)}
A lista legnagyobb értéke: {max(data)}
A lista elemeinek az összege: {sum(data)}
A lista elemeinek az átlaga: {sum(data) / len(data)}
""")
