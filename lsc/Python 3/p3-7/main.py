def pyramid():
    bricks = int(input("enter the number of bricks: "))
    height = 0

    while bricks > 0:
        if bricks >= height + 1:
            bricks -= height + 1
            height += 1
        else:
            break

    res = f"The height of the pyramid {height}, and we have {bricks} bricks left."
    print(res)


def chi9gu5():
    """De Morgan identity"""
    p = True
    q = False
    print(not(p and q) == (not p or not q))
    print(not (p or q) == (not p and not q))


if __name__ == '__main__':
    pyramid()
    chi9gu5()
