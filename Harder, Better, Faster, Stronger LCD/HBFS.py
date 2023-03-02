import time
import serial


def main():
    tty = serial.Serial('COM5',9600)
    lirics_file = open("lirics.txt", 'rt')
    for line in lirics_file.read().splitlines():
        if len(line) > 16:
            line = line[0:15] + "123456789" + line[16:]
        tty.write(bytes(line))
        time.sleep(1)
    lirics_file.close()

if __name__ == "__main__":
    main()
