"""
01-30 Palindroma
Feladat leírás:
Egy beolvasott szövegről állapítsuk meg, hogy palindroma-e.
Palindroma az a szöveg, amely előröl és visszafele is ugyanaz. A szóközök és a kis és nagy betűk nem számítanak.
"""
print("Egy sövegről megállapítjuk hogy palidrma-e.")
du = input("Adj meg egy szöveget: ").lower()
is_palidrome = False
if len(du) > 1:
    for x in range(len(du)):
        is_palidrome = du[x] == du[-x-1]
else:
    is_palidrome = False
print("Ez egy palindróma.") if is_palidrome else print("Ez nem egy palindróma.")
