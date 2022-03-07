# pbq 2021.11.03 jelszo.py 2.0

usrnam = "Mays1"
passwd = "iddqd"

def login():
    logon = False
    print("Felhasználónév: ",end="")
    _un = input()
    print("Jelszó: ",end="")
    _pw = input()
    if _un == usrnam and _pw == passwd:
        logon = True
    return logon


def logon(tries):
    if tries == 0:
        return False
    if login():
        return True
    else:
        print("Próbáld újra!")
        logon(tries-1)

if logon(3):
    print("- [ B E L É P T E T V E ] -")
else:
    print("Bejelentkezési hiba")


