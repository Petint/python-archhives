"""
04-01 Lista információk
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
data = [3, 45, 6, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98, 69]
print(f"""
A lista elemeinek száma :                        {len(data)}
A lista első eleme :                             {data[0]}
A lista utolsó eleme :                           {data[-1]}
A lista harmadik és ötödik elemének az összege : {data[2]+data[4]}
A lista legkisebb értékét :                      {min(data)}
A lista legnagyobb értékét :                     {max(data)}
A lista elemeinek az összegét :                  {sum(data)}
A lista lista elemeinek az átlagát :             {sum(data) / len(data)}
    """)
