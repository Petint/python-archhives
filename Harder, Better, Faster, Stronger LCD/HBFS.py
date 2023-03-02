import time
import serial


def main():
    tty = serial.Serial('COM5',9600)
    lirics_file = open("lirics.txt", 'rt')
    for line in lirics_file.read().splitlines():
        line, line_time = line.split('??')
        if len(line) > 16:
            line = line[0:16] + "123456789123456789123567" + line[16:]
        print(line)
        tty.write(bytes(line, encoding="UTF-8"))
        time.sleep(int(line_time))
    lirics_file.close()
    tty.close()

if __name__ == "__main__":
    main()
