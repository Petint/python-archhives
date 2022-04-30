"""def new_file():
    my_file = open("sheet.txt", "w+")
    my_file.write("So it goes - Vonnegut\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()"""


def file_append():
    my_file = open("sheet.txt", "a+")
    my_file.write("So it stops - Unknown/me\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()


# new_file()
