def stuffs():
    try:
        x = float(input('Adj meg egy számot: '))
    except ValueError:
        print("Nem számot adtál meg.")
    else:
        calcd = 2 * x ** 4 + 3 * x ** 3 + 2 * x ** 2 + 7 * x + 4
        print(calcd, x)
    finally:
        print("Program vége.")


def masodpercbol_ido(secs: int) -> str:
    perc = secs // 60
    ora = secs // 3600
    perc -= ora * 60
    masodperc = secs - 3600 * ora - 60 * perc
    nap = ora // 24
    ora %= 24
    napido = f'{nap}:{ora}:{perc}:{masodperc}'
    return napido


print(masodpercbol_ido(int(input("Add meg hogy hány másodperc telt el a napbol: "))))
