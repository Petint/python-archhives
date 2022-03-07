# celtalan01.py pbq 10a 20201110
# olvassunk be szöveget
# írjuk ki hogy van e benne "a" betű
testfor = "a"
gtxt = input("Adj egy söveget> ")
numa = gtxt.count(testfor)
print(f"A szöveg {numa} {testfor}-beűt tartalmaz.") if numa > 0 else print(f"A szöveg nem tartalmaz {testfor}-betűt.")
