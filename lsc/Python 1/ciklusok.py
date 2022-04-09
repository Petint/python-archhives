import random

print("1. feladat")
szamok = 0
"""while True :
    print(szamok)
    szamok += 1"""
print("2. feladat")
szum = 0
while szamok < 11:
    szum += szamok
    szamok += 1
    print(szum, szamok)
print("3. feladat")
num = 93794361
count = 0
valasz = "vesztettél!"
while num > 0:
    num //= 10
    count += 1
print("numger of digits:", count)
print("4. feladat")
num = random.randint(1, 100)
kerdes = int(input("Hány tippet akarsz?\n> "))
while kerdes >= 1:
    tipp = int(input("tipp:\n> "))
    kerdes -= 1
    if tipp == num:
        valasz = "Nyertél!"
        break
    elif tipp > num:
        print("kisebb")
    else:
        print("nagyobb")
print(valasz)
print("5. feladat")
num1 = 0
num2 = 1
times = int(input("hány szám?\n> "))
while times > 0:
    print(str(num1) + "\n")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    times -= 1
