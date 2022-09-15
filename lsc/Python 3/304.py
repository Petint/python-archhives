print(123, 123)
print(oct(123), 0o123)
print(hex(123), 0x123)
print(bin(123), 0b011011)

a = 0.00000002
print(a)
b = 2e+30
print(b)

try:
    i = int(input("Aggy meg egg sámoty"))
    f = int(input("Aggy meg egg sámoty"))
except ValueError:
    print("nyem sámoty attyáj megy")
else:
    if i > f:
        print(i, "y", f)
    if i < f:
        print(i, "í", f)
    else:
        print("á ketty samv egenlo")
