# pbq 20201110 10a
import petint
x = "dfd"
while x != "":
    x = input("Adj egy számot:  ")
    if(x.isnumeric()):
        print("Nem szám")
    else:
        print(x)

    