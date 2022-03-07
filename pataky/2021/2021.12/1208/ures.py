stra = input()
words = open("words.tyt","wt")
while stra != "":
    stra = input()
    if 'a' in stra or 'A' in stra:
        words.write(stra+'\n')
words.close()
