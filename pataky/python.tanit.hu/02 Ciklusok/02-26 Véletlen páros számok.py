"""Generáljon le 10 random kétjegyű, páros egész számot! Minden szám csak egyszer szerepelhet"""
from random import randint
numbers = []
while len(numbers) < 10:
    number = randint(10, 99)
    if number % 2:
        pass
    else:
        numbers.append(number)
print('A gernerált elemek:')
for number in sorted(numbers):
    print(number, end='\t')
print('')
