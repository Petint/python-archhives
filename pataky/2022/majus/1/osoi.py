path = "magyar-koltok-irok.txt"
file = open(path, "r", encoding="utf-8")
fdata = file.read()
# print(fdata)
fdata = fdata.splitlines()
irok_file = open("irokfile.tyt", "wt", encoding="utf-8")
for ember in fdata:
    if "költő" in ember and "író" in ember:
        print(ember)
        irok_file.write(ember+'\n')
file.close()
irok_file.close()
