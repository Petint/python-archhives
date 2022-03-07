# 1.py 2021 11 15 pbq 10.Aa
# egy program amiben szerepel egy lisrtába 5 tetszőleges szám
nums = [420, 69, 1221, 555, 666]
#végig menni a lista elemein, kiírni hogy páros-e.

for num in nums:
    print(num,end="\t")
    print("páros") if num % 2 else print("Nem páros")

