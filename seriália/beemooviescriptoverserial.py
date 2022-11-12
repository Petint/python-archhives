import serial

with open('beemooviescript.txt', encoding='utf-8') as bmsf:
    bees = bmsf.read()
com = serial.Serial('COM1', 9600)
for bee in bees.splitlines():
    com.write(bee)
