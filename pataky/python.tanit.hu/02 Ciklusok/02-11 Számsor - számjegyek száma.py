"""
Olvassunk be egy egész számot. Amíg a felhasználó nem egész számot ad meg, addig próbálhatja újra.
Ha üres sztringet ad meg, akkor vége a programnak.
Minden esetben, amikor egész számot ad meg, írjuk ki hány jegyű a szám.
Minden esetben írd ki a program végén, hogy "Viszlát!"
"""

print('Adj meg egész számokat és megállapítjuk róla hány jegyű. Ha nemn akarsz tippelni csak nomj sima entert.')
tip = -1
while True:
    tip = input('Adj meg egy számot: ')
    if tip == '':
        break
    print(f'A megadott szám {len(tip)} jegyű.')
print('Viszlát!')
