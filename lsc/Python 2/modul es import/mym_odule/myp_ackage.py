def sumn(a, b):
    return a + b


def avrg(a, b):
    return (a + b) / 2


def powr(a, b):
    return a ** b


def primes(p):
    primes = []
    for i in range(p):
        isprime = True
        for j in range(2, i//2 + 1):
            if i % j == 0:
                isprime = False
                continue
        primes.append(i) if isprime else print("Not prime",end="\t")
    print("\n")
    return primes


def mkmtx(y,x):
    return [[0 for i in range(x)] for i in range(y)]

