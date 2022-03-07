from random import randint as randy

luke = randy(0,9)

tippmax = 5

def guessing(guess):
    global tippmax
    if guess == luke:
        print("Talált!")
        exit()
    elif tippmax <= 1:
        print("Nem talált!")
        exit()
    else:
        tippmax-=1
        guessing(int(input("Adj egy számot> ")))


guessing(int(input("Adj egy számot> ")))
