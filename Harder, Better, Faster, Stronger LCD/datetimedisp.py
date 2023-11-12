import datetime
import serial


def main():
    tty = serial.Serial('COM1', 9600)
    tty.write(b'<ID01>')
    screen = b'<ID01>'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M").encode()
    tty.write(screen)
    print(screen)
    tty.close()


if __name__ == '__main__':
    main()
