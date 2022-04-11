print('1. Feladat')
for x in range(1, 10):
    print(x)
print("2. feladat")
for x in range(1, 11):
    print(x)
print("3. feladat")
for x in range(2, 18, 2):
    print(chr(x))
print("4. feladat")
for x in "Hello, world!":
    print(x)
print("5. feladat")
_input = int(_input("Adj meg egy számot:\n>"))
for x in range(2, 11):
    print(x * _input)
print("6. feladat")
titkos = "Wyh earne  eclaenp hIa nbtu?"
uzenet = ""
for x in range(1, len(titkos)):
    if x % 2 == 0:
        uzenet += titkos[x]
for x in range(1, len(titkos)):
    if x % 2 == 1:
        uzenet += titkos[x]
print(uzenet)
print("7. feladat")
_input = "szia, retek.py vagyok"
elso, masodik = _input[:(len(_input) - 1) // 2], _input[(len(_input) + 1) // 2:]
szoveg = ""
for r in range((len(_input) - 1) // 2):
    szoveg += elso[r]
    if r < len(masodik):
        szoveg += masodik[r]
print(szoveg)
