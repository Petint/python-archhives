# 1. feladt

def RecursiveOne(num):
    print(num)
    if num > 0:
        num -= 1
        RecursiveOne(num)


# RecursiveOne(10)

# 2. faktoriális
def factorecursive(n):
    if n == 0:
        return 1
    else:
        return factorecursive(n-1)

# 3. fib. számok
def reccunacchi(n):
    print(f"Calcullating F({n})", end=", ")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return reccunacchi(n-1) + reccunacchi(n-2)

"""
for x in range(11):
    reccunacchi(x)
"""

# 3. harmonikuss sorozat


def reharmosieve(n):
    if n == 1:
        return n
    else:
        return 1 / n + reharmosieve(n-1)


# print(reharmosieve(3))

# +1: rekurzív hatvány

def recursive_hatvany(x,y):
    if x == 1:
        return 1
    elif y == 0:
        return 1
    elif x == 2 and y == 2:
        return 4
    elif y == 0:
        return x
    else:
        return recursive_hatvany(x,y-1)


print(recursive_hatvany(444,0))