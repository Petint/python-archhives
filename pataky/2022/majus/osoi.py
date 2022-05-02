print('kiírjuk a költőket tartalmát.')
path = "magyar-koltok-irok.txt"
file = open(path, "r", encoding="utf-8")
fdata = file.read()
# print(fdata)
fdata = fdata.splitlines()
for ember in fdata:
    if "költő" in ember:
        print(ember)
file.close()
