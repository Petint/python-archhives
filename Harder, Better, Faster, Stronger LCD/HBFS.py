import time
import serial


def main():
    tty = serial.Serial('COM5',9600)
    lirics_file = open("lirics.txt", 'rt')
    for line in lirics_file:
        tty.write(line.strip('\n'))
        time.sleep(1)
    lirics_file.close()

if __name__ == "__main__":
    main()
