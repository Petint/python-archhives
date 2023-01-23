"""
Egészítsd ki a mellékelt programot úgy, hogy az abban a szereplő két listáról (data1, data2) állapítsd meg:
1. Melyik listának van több eleme
2. Hányadik számnál van az első eltérő elem
3. Melyikben szerepel többször a 10-es szám
4. Melyiknek nagyobb az elemei átlaga
Akkor is helyesen működjön a program, ha módosítjuk a két listát!
"""

# Tájékoztatjuk a felhasználót, hogy hogyan működik a program
print('Két lista elemeit vetjük össze.')

# Az előre megadott két lista
data1 = [3, 45, 10, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98, 4, 7, 65, 10, 98, 3, 23, 53, 16, 763, 9, 495, 6, 7,
         87, 53, 165, 34, 79, 52, 36, 77, 521, 243, 34, 56, 765, 34, 23, 125, 7, 5, 34, 8, 234, 31, 3]
data2 = [3, 45, 10, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98, 4, 7, 65, 10, 98, 3, 23, 53, 16, 763, 9, 465, 6, 7,
         87, 53, 165, 34, 79, 79, 52, 10, 8, 77, 521, 243, 34, 56, 765, 10, 23, 125, 7, 5, 6, 34, 8, 234, 31, 3]

print('A \'data1\' listának', end=' ') if len(data1) > len(data2) else print("A \'data2\' listának", end=' ')
print("tőbb eleme van a másiknál.")

x = -1
run = True
while run:
    x += 1
    run = data1[x] == data2[x]
print(f"Az első eltérő elem: {x + 1}")

print('A \'data1\' lista', end=' ') if data1.count(10) > data2.count(10) else print("A \'data2\' lista", end=' ')
print("tőbb 10-et tartalmaz a másiknál.")

average1, average2 = sum(data1) / len(data1), sum(data2) / len(data2)
print('A \'data1\' listának', end=' ') if average1 > average2 else print("A \'data2\' listának", end=' ')
print("magasabb átlaga van a másiknál.")
