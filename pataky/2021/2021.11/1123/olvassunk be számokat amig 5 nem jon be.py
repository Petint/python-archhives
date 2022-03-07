import numpy as np
run = True
nums = []
for x in range(5):
    nums.append(int(input("Írj be egy számot# ")))

mxa, mix = np.max(nums), np.min(nums)
atl, sum = np.average(nums), np.sum(nums)
print(f"{mxa} volt a legnagyobb és {mix} volt a legkisebb szám")
print(f"{atl} volt az átlaga és {sum} volt a számok összege.")
