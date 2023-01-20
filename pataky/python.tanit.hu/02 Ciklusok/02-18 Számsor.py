"""
Olvassunk be öt egész számot. A végén írjuk ki melyik a legnagyobb és melyik a legkisebb.
Írjuk ki a számok összegét és átlagát is. Ezekhez használd a Python függvényeit.
Biztosra vehetjük, hogy a felhasználó egész számokat ad meg.
"""

print('Kérünk öt számot. Ki fogjuk írni a legkisebbet, a legnagyobbat, az összegüket és az átlagukat.')
numbers = [int(input('Adj meg egy számot:')) for _ in range(5)]
print('A legkisebb', min(numbers)), print('A legnagyobb', max(numbers))
print('Az összegük', sum(numbers)), print('Az átlaguk', sum(numbers)/5)
