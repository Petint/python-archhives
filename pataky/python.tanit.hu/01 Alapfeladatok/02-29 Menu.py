"""
A felhasználó három lehetőség közül választhasson:
a) Kiírjuk neki az első 10 páros számot
b) Kérünk töle egy számot, és megmondjuk, hogy az páros-e
c) Kérünk tőle két számot és kiírjuk a szorzatukat
d) Kilépés a programból

Addig kérjük ismétlődően a menüből választást, amíg d-vel ki nem lép.
"""


def paros(num: int):
    if num % 2 == 0:
        print("A szám páros.")
    else:
        print("A szám páratlan.")


def parios():
    for x in range(0, 20, 2):
        print(x, end=", ")
    print("\n")


run = True
while run:
    # Tájékoztatjuk a felhasználót
    print("""
Menü
A) Páros számokat írunk ki
B) Egy számrol megmondjuk hogy páros-e
C) Szorzatot számolunk.
D) Kilépés
    """)

    todo = input("Válassz [a, b, c, d]>").lower()
    match todo:     # I know match wasn't ment for this. I just wanted to try it out.
        case "a":
            parios()
        case "b":
            paros(int(input('Adj meg egy számot> ')))
        case "c":
            print(int(input("Adj meg egy számot> ")) * int(input("Adj meg egy számot> ")))
        case "d":
            run = False
            print("Viszlát!")
        case _:
            print(f"Nincs ilyen opció: \"{todo}\"")
