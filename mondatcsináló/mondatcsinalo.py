import random
inputFlie = open("input.txt","r",2048,"utf-8")
ki = inputFlie.readline().split(",")
hol = inputFlie.readline().split(",")
mivel = inputFlie.readline().split(",")
mit = inputFlie.readline().split(",")
i = 0

print(f"{ki[random.randint(0,len(ki)-2)]} {hol[random.randint(0,len(hol)-2)]} {mivel[random.randint(0,len(mivel)-2)]} {mit[random.randint(0,len(mit)-2)]}.\n")
