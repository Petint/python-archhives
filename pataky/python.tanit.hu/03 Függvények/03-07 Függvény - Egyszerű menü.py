"""
Feladat leírás:
Olvassunk be egy szöveget.
Kérdezzük meg a felhasználót, hogy mit szeretne:
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát
Addig ismételjük a fentebb írtakat, amíg üres szöveget nem ad meg a felhasználó.
Egy lehetséges megoldást itt találsz.
"""


def main():
    du = 0
    while du is not None:
        du = du_input()
        if du is not None:
            du_text = input("Addj meg egy szoveget: ")
            if du == 1:
                abetu(du_text)
            if du == 2:
                szoveghossz(du_text)
            if du == 3:
                nagybetu(du_text)
    print('Viszlat!')


def du_input():
    print("""
mit szeretne?
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát
    """)
    dear_user = input('>')
    if dear_user.lower() == 'a':
        return 1
    elif dear_user.lower() == 'b':
        return 2
    elif dear_user.lower() == 'c':
        return 3
    else:
        pass


def abetu(text: str):
    print(f'Az adott szovegben az a betu {text.count("a")}-szor/-szer jelenik meg.')


def szoveghossz(text: str):
    print('A szoveg hossza:', len(text))


def nagybetu(text: str):
    print(text.upper())


if __name__ == '__main__':
    main()
