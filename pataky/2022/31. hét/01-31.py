print("Két beolvasott egész számról állapítjuki meg, hogy mely szám a nagyobb.")
nums = int(input("Adj meg egy egész számot: ")), int(input("Adj meg egy egész számot: "))
print(f"""
{nums[0]}+{nums[1]}={nums[0] + nums[1]}
{nums[0]}-{nums[1]}={nums[0] - nums[1]}
{nums[0]}*{nums[1]}={nums[0] * nums[1]}
{nums[0]}/{nums[1]}={nums[0] / nums[1]}, két tizedesre kerekítve: {round(nums[0] / nums[1], 2)}
""")
