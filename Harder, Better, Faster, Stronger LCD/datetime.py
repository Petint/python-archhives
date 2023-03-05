import datetime
import serial


def main():
    tty = serial.Serial('COM5', 9600)
    tty.write(b'0') # datetime.datetime.now().strftime("%Y-%M-%D %H:%M")
    screen = "2023-01-01 00:00"
    tty.write(bytes(screen, encoding="utf-8"))
    print(screen)
    tty.close()


if __name__ == '__main__':
    while True:
     main()
