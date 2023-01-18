"""
Kérjen be 2 két szöveget a felhasználótól, döntse el, hogy melyik a hosszabb és mennyivel!
"""
print('Két megadott szövegről állapítjuk meg, hogy melyik a hosszabb és mennyivel')
number_1 = input('adj meg egy szöveget: ')
number_2 = input('Adj meg még egy szöveget: ')
diff = len(max(number_1, number_2)) - len(min(number_1, number_2))
if len(number_1) > len(number_2):
    print('Az első szöveg hosszabb, ', end='')
elif len(number_1) < len(number_2):
    print('A második szöveg hosszabb, ', end='')
else:
    print(f'A két szám egyforma hosszú.')
if diff != 0: print('ennyivel:', diff)
