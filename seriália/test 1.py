import serial
ser = serial.Serial('com1')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
line = ser.readline()   # read a '\n' terminated line
print(line.decode())
ser.close()             # close port