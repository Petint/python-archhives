def openchars():
    """Beolvassa egy file tartalmát"""
    file = open("pythontextfile.txt","rt",encoding="utf-8")
    print(file.read(8))
    file.seek(0)
    print(file.read(8))
    file.close()


def openlines():
    """Sorokat olvas be egy file-ból"""
    file = open("pythontextfile.txt","rt",encoding="utf-8")
    lines = file.readline()
    for line in lines:
        print(line,end="")
    file.close()


def opencfl():
    "Sorok részeit írja ki"
    file = open("pythontextfile.txt","rt",encoding="utf-8")
    lines = file.readline()
    for line in lines:
        print(line[2:4])
    file.close()


def findtext():
    with open("pythontextfile.txt") as f:
        if "Harry" in f.read():
            print("Harry szereple az első oldalon.")
        else:
            print("Harry nem szereple az első oldalon.")


def createfile(filename:str):
    """Létrehoz egy üres file-ot, paraméter által meghatározható névvel."""
    f = open(filename+".txt","wt+")
    f.write("mmmmmmmmm")
    f.seek(0)
    print(f.read())
    f.close()


def rmsps():
    """Remove spaces from text file."""
    f1 = open("pythontextfile.txt","rt")
    fns = open("nsp.txt","w+")
    txt = f1.read().replace(" ","")
    f1.close()
    fns.write(txt)
    fns.seek(0)
    print(fns.read())
    fns.close()


def lastline(n):
    f = open("pythontextfile.txt","rt",encoding="utf-8")
    lines = f.readline()
    while n > 0:
        print(lines[-n], end="")
        n-=1
    f.close()


def fappend():
    """Append to eof"""
    fi = open("nsp.txt","at+")
    fi.write("\nDis iz an ew 'ine.")
    fi.close()
# openchars()
# openlines()
# opencfl()
# findtext()
# createfile("Gyilkos")
# rmsps()
# lastline(66)
# fappend()