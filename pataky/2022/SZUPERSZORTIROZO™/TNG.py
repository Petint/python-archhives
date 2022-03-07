#Test number generator
import random

OutFile = open("out.txt","x")

for x in range(1000001):
    OutFile.write(str(random.uniform(-10000,10000))+"\n")
OutFile.close()
print('Done')
