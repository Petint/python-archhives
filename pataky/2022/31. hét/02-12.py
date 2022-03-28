from random import randint

nums = []

while 1 not in nums:
    nums.append(randint(0,9))
print(f"""
Egyjegyű véletlen számokat generálunk egészen addig, amíg az 1-es ki nem jön.
a generált számok: {nums}
Ahányadikra az 1-es szám kijőtt: {nums.index(1) + 1}
""")
