from PetintLib import petint, autotable, gagyimatek

if __name__ == '__main__':
    input("Testing autotable.py...")
    size = 30
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    table1 = autotable.Table(test_data)
    print(table1.make())

    input("Testing gagyimatek.py...")
    print(gagyimatek.osszead(5, 5))
    print(gagyimatek.kivon(5, 5))
    print(gagyimatek.szorzas(5, 5))
    print(gagyimatek.oszt(5, 5))
    print(gagyimatek.hatvany(5, 5))
    print(gagyimatek.__all__)
    input()

    input("Testing petint.py...")
    print(petint.filetofloat('asd'))
