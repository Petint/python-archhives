path = "magyar-koltok-irok.txt"
file = open(path, "r", encoding="utf-8")
fdata = file.read()
# print(fdata)
fdata = fdata.splitlines()