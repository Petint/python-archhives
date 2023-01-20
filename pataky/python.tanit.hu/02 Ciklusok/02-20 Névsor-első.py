"""Olvass be öt angol nevet és írd ki a névsorban legelsőt."""
print('Öt angol névről állapítjuk meg, hogy melyik a legelső a návsorban.\nAz első nev a névsor szerint:',min([input('Adj meg egy angol nevet:') for _ in range(5)]))
