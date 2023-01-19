"""
Kérjük be hány egész számot akar megadni a felhasználó majd annyi egész számot beolvastatunk és aztán kiírjuk a legkisebbet.
Biztosra vehetjük, hogy egész számot adnak meg az elején is és utána is.
"""
print('Annyi számot olvasunk be, ahányat az elején megadsz, utána kiírjuk a legkisebbet közölük.')
count = int(input('Hány egész számot szeretnél megadni?:'))
numbers = [int(input('Adj meg egy számot: ')) for _ in range(count)]
print('A legkisebb szám:', min(numbers))
