import time
# import Serial


def main():
    # tty = Serial.Serial('COM5',9600)
    lirics_file = open("lirics.txt", 'rt')
    for line in lirics_file:
        print(line.strip('\n'))
        time.sleep(1)
    lirics_file.close()

if __name__ == "__main__":
    main()
