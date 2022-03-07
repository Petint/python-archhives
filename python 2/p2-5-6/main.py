# matrix example 1.
from random import randint

matrixi = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 14, 14]
]


def printmat(matrix):
    for matx in matrix:
        print(matx)


# 2. matrix filler

white_goop = []

for x in range(0,100):
    temp = []
    for y in range(0,100):
        temp.append(y)
    white_goop.append(temp)
del temp
printmat(white_goop)

# mixxd salad:

api_jani = [
    [1, True, "Sentinel", 1.00002],
    ['rjx', 68, "Vien hbf.", "Budapest-keleti"],
    ["Walter White", 52, "Druglord", False],
    ["The guy that wanted to turn Morpheus in", True, 36,54]
]

print("Before: ")
#printmat(api_jani)

row = -1
while row < 0 or row > 3:
    row = int(input("col number:"))

col = -1
while col < 0 or col > 3:
    col = int(input("col number:"))

change_to = input("change item to: ")
change_type = input("wizch tfype?M [bool, int, str]: ").lower()


def typews(inpt,typ):
    if typ == "bool":
        if inpt == "true":
            return True
        else:
            return False
    elif typ == "int":
        return int(inpt)
    else:
        return inpt


api_jani[row][col] = typews(change_to, change_type)
#printmat(api_jani)


# nice
for x in range(3):
    print("")
# foci

d8a = ["shirt number", "name", "age", "height", "weight"]
ateam = [
    [52,"GÍreti",23,183,73],
    [11,"janka",22,176,70],
    [22,"apfuizget",21,176,65],
    [1,"dori",53,43,123],
    [13,"lisa",567,456,3456]
]


for i in range(len(ateam)):
    for j in range(len(ateam[i])):
        print(ateam[i][j],end="\t")
    print("")
def sorting_mat():
    mat = []
    for i in range(5):
        temp= []
        for j in range(5):
            temp.append(randint(1,10))
        mat.append(temp)
    del temp
    printmat(mat)
    print("\n\n")
    """for matx in mat:
        temp = matx.sort"""
    mat.sort()
    printmat(mat)


sorting_mat()


