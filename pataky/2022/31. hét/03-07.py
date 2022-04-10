def ask_du():
    print("""
Válassz:
a)  Kiírjuk hány "a" betü van a szövegben
b)  Kiírjuk a szöveg hosszát
c)  Kiírjuk a szöveg nagybetűs változatát
D)  Kiírunk valamit
    """)
    du_in = input("Válassz [a, b, c]: ")
    opt = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    try:
        return opt[du_in]
    except KeyError:
        print("Nincs ilyen opcio.")
        pass


def du_text():
    _du = input("Adj meg egy tetszőleges szöveget: ")
    if _du == '':
        del _du
        pass
    else:
        return _du


def abetu(txt: str):
    print("Az adott szöveg \'a\'-betű tartalma", end=": ")
    print(txt.lower().count('a'))


def szhossz(txt: str):
    print("A szöveg hossza", end=": ")
    print(len(txt))


def nagybetu(txt: str):
    print("A nagybetüs verzió", end=": ")
    print(txt.upper())


def chingus(du_txt: str):
    for _chingus in du_txt:
        print('Chingus')


def menu():
    print('A program bekér egy szöveget és a választásod alapján kiír ezt-azt a szövegről. Üres szövegre leáll.\n')
    du_txt = du_text()
    if du_txt is None:
        print('Viszlát!')
        exit()
    else:
        dun = ask_du()
        if dun == 1:
            abetu(du_txt)
        elif dun == 2:
            szhossz(du_txt)
        elif dun == 3:
            nagybetu(du_txt)
        elif dun == 4:
            chingus(du_txt)


if __name__ == "__main__":
    while True:
        menu()
