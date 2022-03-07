ussr = "geza"
pswr = "1234"
nug = 5


def getusr(_usr,guess):
    # for x in range(nug):
    du = input("Felhasználónev: ")
    if du == _usr:
        return True
        # print("Rossz név")
    return False


def getpw(_pass,guess):
    # for x in range(nug):
    du = input("Jelszó: ")
    if du == _pass:
        return True
        # print("Hibás jelszó")
    return False

run = True
while nug > 0 and run:
    if getusr(ussr,nug) and getpw(pswr,nug):
        print("Beléptetve")
        run = False
    else:
        print("Hibás jelszó, vagy felhasználónev!\nPróbáld meg újra!")
        nug -= 1
