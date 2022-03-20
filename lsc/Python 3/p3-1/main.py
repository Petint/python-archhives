words = {"macska": "cicu", "kutya": "kutyesz"}
p_num = {"Mady": "06807781223"}


"""def nincsaron():
    words2 = ["macska", "kutya", "Balász Áron"]
    for word in words2:
        if word in words:
            print(word + "-->" + words[word])
        else:
            print("nincs ilyen elem")


animalz = {
            "cat": "kazte",
            "dog": "hund",
            "horse": "pferd"
}

for key in sorted(animalz.keys()):
    print(key, "-->", animalz[key])

for english, german in animalz.items():
    print(f"{english} --> {german}")

for german in animalz.values():
    print(german)

animalz["cat"] = "cirmike"
animalz["sawn"] = "schwan"
animalz.update({"duck": "ente"})
for english, german in animalz.items():
    print(f"{english} --> {german}")

del animalz["dog"]
animalz.popitem()
# print(animalz)

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}

for d in (dict1, dict2, dict3):
    dict4.update(d)

for english, german in dict4.items():
    print(f"{english} --> {german}")
"""

students = {}
while True:
    name = input("Enter name:   ")
    if name == "":
        break

    score = int(input("Enter score: "))
    if name not in students:
        students[name] = (score, )
    else:
        students[name] += (score, )
for name in sorted(students.keys()):
    add = 0
    kantor = 0
    for score in students[name]:
        add += score
        kantor += 1
    print(name, ":", add / kantor)
