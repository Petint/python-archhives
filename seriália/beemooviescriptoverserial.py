import serial

with open('beemoveiscript2.txt', 'rb') as bmsf:
    bees = bmsf.read()
com = serial.Serial('COM6', 9600)
for bee in bees.splitlines():
    com.write(bee + b'\n\r')
    print(bee)
com.close()
