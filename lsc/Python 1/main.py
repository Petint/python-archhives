print("4.feladat")
x1 = 10
x2 = 5
y1 = "szilva"
y2 = "szilvalekvár"
print(y1 is y2)
print("5.feladat")
print(y1 in y2)
print("6.feladat")
email = input("adj meg egy email cimet.\n>") #lekvaros.kenyer@almafa.hu
if "@" in email and (email.endswith(".com") or email.endswith(".hu")):
    print("Ez az email jó.")
else:
    print("ez az email nem jó.")
print("7. fladat")
a1 = 5
a2 = 3
if a1 < a2:
    print(f"a(z) {a1} kisebb mint a(z) {a2}.")
else:
    print(f"a(z) {a1} nagyobb mint a(z) {a2}.")

