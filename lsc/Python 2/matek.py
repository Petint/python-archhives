

def bitop():
    print(bin(14))
    print(bin(6))
    print(0xa & 0xf) # AND
    print(16 | 4)   # OR
    print(0xff ^ 0xff) # XOR
    print(~0xa) # NOT
    print(14 >> 2, 14 << 2) # shift


def ipaddr():
    ip = [0xc0, 0xa8, 0xa, 0x1]
    mask = [0xff, 0xff, 0xff, 0]
    print("IP cím", end=": ")
    for i in ip:
        print(i, end=".")
    print()
    print("Alháló maszk", end=": ")
    for i in mask:
        print(i, end=".")
    print()
    print("Hálócím", end=": ")
    for x in range(len(ip)):
        print(ip[x] & mask[x], end=".")
    print("")


ipaddr()
