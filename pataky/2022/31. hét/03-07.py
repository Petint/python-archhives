def ask_du():
    print("""
Válassz:
a)  Kiírjuk hány "a" betü van a szövegben
b)  Kiírjuk a szöveg hosszát
c)  Kiírjuk a szöveg nagybetűs változatát
    """)
    du_in = input("Válassz [a, b, c]: ")
    opt = {'a':1,'b':1,'c':3}
    return opt[du_in]


def du_text():
    _du = input("Adj meg egy tetszőleges szöveget: ")
    if _du == '':
        del _du
        pass
    else:
        return _du


def abetu(txt: str):
    pass

def szhossz(txt: str):
    pass


def nagybetu(txt: str):
    pass


def menu():
    print('A program bekér egy szöveget és a választásod alapján kiír ezt-azt a szövegről. Üres szövegre leáll.\n')
    du_txt = du_text()
    if du_txt is None:
        exit()
    else:
        dun = ask_du()
        if dun == 1:
            abetu(du_txt)
        elif dun == 2:
            szhossz(du_txt)
        elif dun == 3:
            nagybetu(du_txt)

if __name__ == "__main__":
    menu()
