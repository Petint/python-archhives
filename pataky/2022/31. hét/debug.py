from random import randint

x = int(input('Adj meg egy számot: '))
y = x * 2
print(f'A szám duplája: {y}')

randomnums = []
for _ in range(100):
    x = randint(0, 100)
    randomnums.append(x)
print(randomnums)

x = input('adj meg egy szöveget: ').lower()
mhangzo = 'öüóuioőúéáűíae'
magnozo = 'qwertzpsdfghjklyxcvbnm'
mgnum = 0
mmm = 0
lnt = 0
egyem = 0
szamsz = 0
for i in x:
    if i in mhangzo:
        mgnum += 1
    elif i in magnozo:
        mmm += 1
    elif i.isnumeric():
        szamsz += 1
    else:
        egyem += 1
    lnt += 1
print(lnt, mgnum, mmm, szamsz, egyem, sep='\n')
