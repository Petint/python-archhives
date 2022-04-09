nums = [2, 3, 4, 5, 6, 564, 65, 666, 64, 69, 555, 420]


def Maxx(inpt):
    valuae = inpt[0]
    for c in inpt:
        if c > valuae:
            valuae = c
    return valuae


def Minx(inpt):
    valuae = inpt[0]
    for c in inpt:
        if c < valuae:
            valuae = c
    return valuae


if len(nums) > 0:
    print(f"The biggest number is: {Maxx(nums)}")
    print(f"The smalest number is: {Minx(nums)}")
else:
    print("There was an error.")
