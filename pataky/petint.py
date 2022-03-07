"""
petint 1.2.1
A saját python modul hasznos metódusokkal
és konstansokkal
"""

constants = {
    """kostansok listája"""
    "tnt" : 46,
    "weed": 420,
    "gridparts": ('─','│','┌','┐','└','┘','├','┤','┬','┴','┼')
}

__all__ = ["__all__","constants","du_inpt_int","getmcpi","FileImportFloatList","FileImportStrList",
    "randflist"]


def du_inpt_int(tries,message):
    """Hibakezelős számbekérő"""
    if tries != 0:
        try:
            intptszam = int(input(message))
        except:
            print("Nem számot adtál meg.")
            intptszam = du_inpt_int(tries - 1,message)
        return intptszam
    else:
        input("Tul sok hibás próbálkozás.\nA program leáll...")
        exit()


def getmcpi():
    """egyszerű mcpi import"""
    from mcpi.minecraft import Minecraft
    _mc = Minecraft.create()
    print("mcpi importálva")
    _mc.postToChat("Import successfull")
    return _mc


def FileImportFloatList(FileName):
    """File import hibakezeléssel
    float listaként
    """
    print("Importind data... ",end="") # Report to DU
    try:
        ImputFile = open('./'+FileName,"rt") # Get file
    except: # If Input file doesn't exist
        print(f"Error, {FileName} can't be found")
        ImputFileError = True
        input()
        exit()
    #return file data as a List of floats
    FileData = ImputFile.read() # Store file contents
    del ImputFile # The variable 'ImputFlie' is no longer needed
    FileDataList = FileData.split('\n')
    # FileDataList = FileDataList.split(',') Broken, don't use.
    del FileData # Delete variable
    FileDataFloat = []
    for x in FileDataList:
        FileDataFloat.append(float(x))
    del FileDataList # Delete old list
    print("Done")
    return FileDataFloat # Return Data as a List of floats


def FileImportStrList(FileName):
    """File import hibakezeléssel
    string listaként"""
    print("Importind data... ",end="") # Report to DU
    global ImputFileError
    try:
        ImputFile = open('./'+FileName,"rt") # Get file
    except: # If Input file doesn't exist
        print(f"Error, {FileName} can't be found")
        ImputFileError = True
        input()
        exit()
    #return file data as a List of floats
    FileData = ImputFile.read() # Store file contents
    del ImputFile # The variable 'ImputFlie' is no longer needed
    FileDataList = FileData.split('\n')
    # FileDataList = FileDataList.split(',') Broken, don't use.
    del FileData # Delete variable
    print("Done")
    return FileDataList # Return Data as a List



def randflist(numOfNums):
    """generate list of random numbers"""
    import random
    out = []
    for x in range(numOfNums):
        out.append(random.uniform(-10000,10000))
    return out

