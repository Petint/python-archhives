def file_read():
    my_file = open("sheet.txt", "r")
    print(my_file.read())
    my_file.close()


def new_file():
    my_file = open("sheet.txt", "w")
    my_file.write("So it goes - Vonnegut\n")
    """my_file.seek(0)
    print(my_file.read())
    my_file.close()"""


def file_append():
    my_file = open("sheet.txt", "a")
    my_file.write("If you try you can fail.\n")
    """my_file.seek(0)
    print(my_file.read())
    my_file.close()"""


def letter_count(p):
    my_file = open("sheet.txt", "r")
    count = 0
    for e in my_file.read():
        if e.lower() == p:
            count += 1
    my_file.close()
    print(count)


def list_file():
    my_file = open("sheet.txt", "w")
    shoppings = ["braad\n", "orang\n", "melk\n", "cheez\n", "soap shoes\n", "shish kebab\n"]
    my_file.writelines(shoppings)


def remove_kebab(p):
    shooping_file = open("sheet.txt", "r+")
    lines = shooping_file.readline()
    shooping_file.seek(0)
    for line in lines:
        if line.strip("\n") != p:
            shooping_file.write(line)
        shooping_file.truncate()
    shooping_file.close()


def file_pattern():
    my_file = open("sheet.txt", "w")
    pointer = 0
    for line in range(20):
        thisline = ""
        for chair in range(6):
            if chair == pointer:
                thisline += "  "
            else:
                thisline += "--"
        if pointer == 5:
            dirt = False
        if pointer == 0:
            dirt = True
        if dirt:
            pointer += 1
        else:
            pointer -= 1
        thisline += '\n'
        my_file.write(thisline)


new_file()
file_append()
letter_count("a")
list_file()
remove_kebab("shish kebab")
file_read()
file_pattern()
