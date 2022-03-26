"""
02-12 Véletlen számsor
Feladat leírás:
Addig generáljunk véletlen egyjegyű számokat, amíg 1-nem lesz. A végén írjuk ki, hányadikra jött ki az 1-es szám.
"""

from random import randint
nums = []
while 1 not in nums:
    nums.append(randint(0, 9))
print(f'{nums.index(1) + 1}. jött ki az 1-es szám.')
