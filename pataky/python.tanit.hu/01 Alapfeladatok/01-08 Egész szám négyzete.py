"""
Kérjen be egy számot a felhasználótól (ellenőrizze, hogy egész szám-e), ha egész szám, akkor írja ki a négyzetét, ha nem, akkor azt, hogy "Nem egész szám!"
"""
print('Egy beolvasott szám négyzetét írjuk ki, vagy azt hogy HIBA, ha nem egész számot adtak meg.')
dear_user_responds = input('Adj meg egy számot: ')
if dear_user_responds.isnumeric():
    print('A szám négyzete:', int(dear_user_responds)**2)
else:
    print('HIBA: Nem egész számot adtál meg!')
