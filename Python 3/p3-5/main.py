myint = 420
mystr = "#Bumpdumplings"
mbool = False
myflt = 3.141
myset = {"Budapest-Nyugati", "Zugló", "Kőbánya alsó", "Kőbánya-kispest", "Kispest", "Pestszentimre felsö",
         "Pestszentimre", "Gyál felső", "Gyál", "Felsőpakony", "Ócsa", "Inács-Kakucs", "Dabas", "Gyón", "Hernád",
         "Örkény", "Táborfalva", "Felsőlajos", "Lajosmizse"}
mytup = (564, "#Itsonlyfriday", True)
mylst = [myint, mystr, myflt, mbool, mytup, myset]
mdict = {'one': 9, 'sevens': 666, 'eight': 123}
mymat = [mylst, mylst, mylst]

print(myint)
print("id", id(myint))
myint = 6
print(myint)
print("id", id(myint))

wat = (1, [2, 3, 4, 5])
print(wat, 'id', id(wat))
wat[1][2] = 6
print(wat, 'id', id(wat))
