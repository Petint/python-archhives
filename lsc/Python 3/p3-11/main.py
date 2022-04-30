def new_file():
    my_file = open("sheet.txt", "w+")
    my_file.write("So it goes - Vonnegut\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()


new_file()
