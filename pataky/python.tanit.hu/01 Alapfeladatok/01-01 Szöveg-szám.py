"""Olvassunk be egy számot. Ha nem egész szám, akkor írjuk ki, hogy "Nem egész szám", különben írjuk ki, hogy "Egész szám"."""
dear_user_responds = input('Egy beolvasot sztringről állapítjuk meg, hogy az egész szám-e vagy sem.\nAdj meg egy számot: ')
if dear_user_responds.isnumeric():
    print('Egész szám')
else:
    print('Nem egész szám')
