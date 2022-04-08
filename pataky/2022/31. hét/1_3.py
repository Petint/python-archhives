#place worlds in new lines.
dog = input("Írj szavakat, vagy kb akármit.\n> ")
dog = dog.replace(" ","\n")
print(dog)

#using split()
dog = input("Írj szavakat, vagy kb akármit.\n> ")
dog = dog.split(" ")
for x in dog:
    if x == "chingus":
        print("hvacrvideos.com")
    else:
        print(x)
