import random

input_file = open("input.txt", "r", 2048, "utf-8")
words = input_file.read().splitlines()
input_file.close()
for i in range(4):
    words[i] = words[i].split(",")
ki = words[0][random.randint(0, len(words[0]) - 2)]
hol = words[1][random.randint(0, len(words[1]) - 2)]
mivel = words[2][random.randint(0, len(words[2]) - 2)]
mit = words[3][random.randint(0, len(words[3]) - 2)]
print(f"{ki} {hol} {mivel} {mit}.\n")
