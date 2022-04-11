titkos = "Wyh earne  eclaenp hIa nbtu?"
uzenet = ""
for x in range(1, len(titkos)):
    if x % 2 == 0:
        uzenet += titkos[x]
for x in range(1, len(titkos)):
    if x % 2 == 1:
        uzenet += titkos[x]
print(uzenet)
