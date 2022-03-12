try:
    x = float(input('Addj meg egy számot: '))
except ValueError:
    print("Nem számot adtál meg.")
else:
    calcd = 2 * x ** 4 + 3 * x ** 3 + 2 * x ** 2 + 7 * x + 4
    print(calcd, x)
finally:
    print("Program vége.")
