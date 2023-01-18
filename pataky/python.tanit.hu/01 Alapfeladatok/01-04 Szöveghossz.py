"""
Olvass be két szöveget és írd ki a rövidebbet. Ha egyforma hosszúak, akkor írd ki, hogy egyformák.
"""

print('Két megadott szövegről állapítjuk meg, hogy melyik a hosszabb')
number_1 = input('adj meg egy szöveget: ')
number_2 = input('Adj meg még egy szöveget: ')
if len(number_1) == len(number_2):
    print(f'A két szám egyenlő!')
else:
    print(f'A hosszabb söveg: {max(number_1, number_2)}')
