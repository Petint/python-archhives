"""
Feladat leírás:
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
print('Egy listarol laaapintunk meg nivfirmaciotka.')
data = [3, 45, 6, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98]
print(f"""
- a lista első eleme: {data[0]}
- a lista utolsó eleme: {data[-1]}
- a lista harmadik és ötödik elemének az összege: {data[2] + data[4]}
- a lista legkisebb értéke: {min(data)}
- a lista legnagyobb értéke: {max(data)}
- a lista elemeinek az összege: {sum(data)}
- a lista elemeinek az átlaga: {sum(data) / len(data)}
""")
