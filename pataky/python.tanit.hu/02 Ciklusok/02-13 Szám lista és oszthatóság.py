"""Írd ki az alábbi lista összes elemét először egy sorban, majd külön sorokba azzal együtt, hogy oszthatók-e héttel."""
numList = [2345, 42, 1, 10, 6790, 56, 234, 865, 124, 1638, 76, 145, 742]
for num in numList:
    print(num, ' - ', 'nem ' if num % 7 else '', 'osztható héttel', sep='')
