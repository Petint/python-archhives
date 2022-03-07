# szamkitalalo.py pbq 20211110
# gondoltam egy számot 1 és 5 közt. Ki tudod találni?
from petint import du_inpt_int as rd
from random import randint as randy

rar = randy(1,5)
guess = -1
tries = 0
while guess != rar:
    tries += 1
    guess = rd(3,"gondoltam egy számot 1 és 5 közt. Ki tudod találni?\n> ")
    if guess != rar:
        print("Nem erre a számra gondoltam!")
print(f"Nyertél! \n{tries} probálkozásra volt sükséged!")
