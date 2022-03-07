# 1109.py pbq10a 20211109
def du_inpt(tries):
    if tries != 0:
        try:
            intptszam = int(input("Adj egy számot: "))
        except:
            print("Nem számot adtál meg.")
            intptszam = du_inpt(tries - 1)
        return intptszam
    else:
        input("Tul sok hibás próbálkozás.\nA program leáll...")
        exit()

inpt = du_inpt(4)
if inpt % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")
    
