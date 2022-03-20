allat_lab = int(input("Hány lába van?\n>"))
allat_uszni = input("tud uszni?\n>")
allat_repul = input("tud reülni?\n>")
allat_masz = input("tud mászni?\n>")


if allat_lab == 2:
    if allat_repul.lower == "igen":
        if allat_uszni.lower == "igen":
            print("Kacsa")
        else:
            print("Sas")
    elif allat_uszni.lower == "igen":
        print("pingvin")
    else:
        print("ember")
elif (allat_lab == 0 and allat_uszni.lower == "igen") and allat_repul.lower == "nem":
    print("hal")
elif allat_lab == 4:
    if allat_repul.lower == "igen":
        if allat_uszni.lower == "igen":
            print("???")
        else:
            print("Sárkány")
    elif allat_uszni.lower == "igen":
        print("Kutya")
    else:
        print("Tehén")
else:
    print("ilyet nem ismerek.")
