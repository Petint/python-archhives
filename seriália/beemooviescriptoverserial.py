import serial

with open('beemoveiscript.txt', 'rb') as bmsf:
    bees = bmsf.read()
com = serial.Serial('COM1', 9600)
for bee in bees.splitlines():
    com.write(bee + b'\n\r')
