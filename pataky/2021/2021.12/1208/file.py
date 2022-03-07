from random import randint as luke


try:
    fline = open("./szamok.txt","at")
except:
    fline = open("./szamok.txt","xt")

for y in range(50):
    randy = luke(0, 100)
    fline.write(f'{randy}\n')
fline.close()
