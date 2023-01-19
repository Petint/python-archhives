"""Addig generáljunk véletlen egyjegyű számokat, amíg 1-nem lesz. A végén írjuk ki, hányadikra jött ki az 1-es szám."""
from random import randint

numbers = []
while 1 not in numbers:
    numbers.append(randint(0, 9))
print(f'Az 1-es szám {len(numbers)}. ként jött ki.')
