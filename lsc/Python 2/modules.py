import math
import random
import matplotlib.pyplot as plt

print(math.pi)
print(math.tau)
print(math.e)
print(math.inf)
print(math.nan)


# 2. kör kerülete, felület
def circlotron(r):
    ker = r*math.tau
    fel = math.pow(r,2)*math.pi
    print(f"A kör kerülete: {round(ker,3)}, a kör felülete: {round(fel,5)}")
    del ker
    del fel
    del r


circlotron(3)



# 3. factorial, de egyszerűbben
print(math.factorial(5))
print(math.sqrt(25))


# 4. random
Nums = []
for i in range(0,100):
    Nums.append(random.randrange(0,11,2))
print(Nums)

# input()



# 5. számkitaláló
trys = 6# próbálkozások száma = 7
secret = random.randint(1,101)# titkos szám elrakása
tip = 0
# ellenörzés
def check(tri,sec,DUin):
    if sec == DUin:
        return "\"I won!\" -Link"
    elif sec < DUin:
        return "Less"
    elif sec > DUin:
        return"More"
    else:
        return "you is lose"
# visszamondás a DU-nak
while tip != secret and trys >-1:
    tip = int(input("Give a number between 1-100.\n: "))
    print(check(trys, secret, tip))
    trys -=1
print("you is lose")

# 6. extra modulok a pip csomagkezelővel
# pip install matplotlib


def PieChart(Size, Lab):
    plt.pie(Size, lables=Lab, autopct="%.2f%%")
    plt.show()


n = int(input("How mani gamez?\n: "))
games = [] # Játékok nevei
likes = []  # Adatok
data = []   # más adatok
db = s = 0

for i in range(n):
    game_name = input("játék neve\n: ")
    like = int(input("Mennnnyyyyire tecccik ez az Lyateékk?(1-10)\n: "))
    db += like
    games.append(game_name)
    likes.append(like)

for i in  range(n):
    s = likes[i] / db * 100
    s = round(s, 1)
    data.append(s)

PieChart(data, games)
