""""
02-07 Függvény - Egyszerű menü
Feladat leírás:
Olvassunk be egy szöveget.
Kérdezzük meg a felhasználót, hogy mit szeretne:
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát

Addig ismételjük a fentebb írtakat, amíg üres szöveget nem ad meg a felhasználó.
"""


def main():
    print(
        """
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát
""")
du = input('Valassz az elozokbol: ')
if du.lower() == 'a':
    acounter()


if __name__ == '__main__':
    main()
