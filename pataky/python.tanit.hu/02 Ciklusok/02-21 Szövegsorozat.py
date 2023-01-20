"""Olvass be szöveget addig, amíg üres sztring nem jön be. A végén írd ki, hogy hány szöveg lett beolvasva."""
print('Szövegeket kérünk tőled, Enter-rel újat adhatast meg. Ha beakarod fejezni, üres szöveget adj meg.')
number_of_texts = 0
text = ' '
while text != '':
    text = input('Adj meg egy szöveget:')
    number_of_texts += 1
print('A beolvasott szövegek száma:', number_of_texts)
