from random import randint


def szamma(tort: 'tuple(int, int)') -> float:
    return tort[0] / tort[1]


nums = [randint(10, 100) for _ in range(4)]
tort1 = nums[0], nums[1]
tort2 = nums[2], nums[3]
del nums
print(f"""
x = {tort1[0]}/{tort1[1]}
y = {tort2[0]}/{tort2[1]}
Állítások:
a) x < y
b) x = y
c) x > y
""")
valasz = input("melyik állítás igaz? ")
valasz = valasz.lower()
nums = [szamma(tort1), szamma(tort2)]
if nums[0] < nums[1]:
    good = 'a'
elif nums[0] == nums[1]:
    good = 'b'
elif nums[0] > nums[1]:
    good = 'c'

if valasz == good:
    print('Helyes válasz')
else:
    print(f'Helytelen válasz, a helyes válasz a {good} volt.')
