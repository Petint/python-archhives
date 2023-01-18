"""
Olvassunk be egy egész számot. Ha nem egész számot adtak meg, érjen véget azzal, hogy kírjuk: "HIBA: Nem egész számot adtál meg!".
Különben írjuk ki a szám dupláját.
"""
print('Egy beolvasott szém dupláját írjzuk ki, vagy azt hogy HIBA, ha nem egész számot adtak meg.')
dear_user_responds = input('Adj meg egy számot: ')
if dear_user_responds.isnumeric():
    print('A szám duplája:', 2 * int(dear_user_responds))
else:
    print('HIBA: Nem egész számot adtál meg!')
