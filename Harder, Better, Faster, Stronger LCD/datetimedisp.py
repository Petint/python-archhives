import datetime
import serial


def main():
    tty = serial.Serial('COM5', 9600)
    screen = datetime.datetime.now().strftime("%Y-%m-%d %H:%M").encode()
    tty.write(screen)
    print(screen)
    tty.close()


if __name__ == '__main__':
    main()
