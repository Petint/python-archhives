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
