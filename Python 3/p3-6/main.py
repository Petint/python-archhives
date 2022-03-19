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

