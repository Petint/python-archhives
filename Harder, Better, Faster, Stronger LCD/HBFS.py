import time
import serial


def main():
    tty = serial.Serial('COM5',9600)
    lirics_file = open("lirics.txt", 'rt')
    for line in lirics_file.read().splitlines():
        if len(line) > 16:
            line = line[0:16] + "123456789123456789123567" + line[16:]
        print(line)
        tty.write(bytes(line, encoding="UTF-8"))
        time.sleep(1)
    lirics_file.close()
    tty.close()

if __name__ == "__main__":
    main()
