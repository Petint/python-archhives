# mynum = int(input("Enter an intiger: "))
mynum = 3
while mynum > 1:
    if mynum % 3 == 0:
        mynum /= 3
    else:
        mynum += 1
    print(mynum)

run = True
i = 0
while run:
    print(i)
    i += 1
    if i > 5:
        run = not run

ddd = ["DAT", "MD", "DCC", "CD", "CC", "LP", "MP3", "FM"]
i = 0
while i > len(ddd):
    print(ddd[i])
    i += 1

mystring = input("e: ")
digits = 0
letters = 0
for x in mystring:
    if x.isdigit():
        digits += 1
    if x.isalpha():
        letters += 1
print(f"digits:{digits}, letters: {letters}")

n = int(input("N-ter de limit: "))

primelist = []
i = 2


"""def isprime(_i: int) -> bool:
    prime = True
    for iDx in range(2, _i):
        if prime _i % iDx == 0:
            prime = False
            break
    return prime


while True:
    if isprime(i):
        primelist.append(i)
    i += 1
    if i == n: 
        break
print(f"prime numbas belo' {n}:")
print(primelist)"""

basket = {
    "apple": 20,
    "pear": 10,
    "banana": 30,
    "chingus": 69
}
friut = input("Enter an fuitr: ")
for item in basket.keys():
    if item == friut:
        print(f"the basketball allready havez {basket[item]} {item}(e)s.")
    else:
        nice = int(input("how mani fruztez? "))
        basket[friut] = nice
        for item2 in basket:
            print(item2, basket[item2], sep=": ")
