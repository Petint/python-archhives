with open('beemoveiscript.txt', 'rt', encoding='UTF-8') as beefile:
    beescript1 = beefile.read().splitlines()
    beescript2 = []
    for beeline in beescript1:
        if beeline not in [y*' ' for y in range(10)]:
            beescript2.append(beeline+'\n')
print(f"Total bees: {len(beescript1)}\nBees aproved: {len(beescript2)}\n"
      f"Bees rejected: {len(beescript1) - len(beescript2)}")
with open('beemoveiscript2.txt', "wt", encoding='UTF-8') as beefile2:
    beefile2.writelines(beescript2)
