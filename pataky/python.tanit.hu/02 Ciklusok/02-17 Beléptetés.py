"""
Tároljunk egy azonosító/jelszó párost. A felhasználónak ezt kell kitalálni. Ha kitalálta, írjuk ki: Beléptetve.
Max 5-ször próbálkozhat. Ha nem találta ki ez idő alatt, akkor írjuk ki: Belépés megtagadva.
"""


def login(tries):
    username = "valami"
    password = "semmi"

    def prompt():
        logon = False
        __username = input('Add meg az azonosítódat:')
        __password = input('Add meg a jelszót:')
        return __username == username and __password == password

    if tries == 0:
        return False
    if prompt():
        return True
    else:
        print("Hibás azonosító vagy jelszó. Próbáld újra!")
        login(tries - 1)


print("Beléptatve!") if login(5) else print("Belápés megtagadva!")
