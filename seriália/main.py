# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser = serial.Serial('COM1', 9600, xonxoff=1)
    ser.write(bytes("Add meg, hogy mi a neved: ", encoding='utf-8'))
    line = ser.readline()
    ser.write(bytes(f'\n\rHi, {line.decode()} \r', encoding='utf-8'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
