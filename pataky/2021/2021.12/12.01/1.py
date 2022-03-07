def dupla(num):
    return 2 * num


def szia():
    print("Szia uram!")


def partlan(num):
    return not (num % 2 == 0)


def szorzó(x,y):
    if str(x).isnumeric() and str(y).isnumeric():
        return x*y
    raise TypeError("Nem számot adtál meg!")   


print(szorzó(12,'a'))
# print(szorzó(int(input(": ")),int(input(": "))))
raise TypeError("XDDFGH")