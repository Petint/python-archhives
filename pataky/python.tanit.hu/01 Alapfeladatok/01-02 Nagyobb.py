"""
Olvass be két egész számot. Írd ki a nagyobbat. Ha egyformák, akkor írd ki, hogy egyenlők.
Biztosra vehetjük, hogy egész számot adunk meg.
"""
print('Két megadott számrol állapítjuk meg, hogy melyik a nagyomm')
number_1 = input('adj meg egy számot: ')
number_2 = input('Adj meg még egy számot: ')
if number_1 == number_2:
    print(f'A két szám egyenlő!')
else:
    print(f'A nagyobb szám: {max(number_1, number_2)}')
