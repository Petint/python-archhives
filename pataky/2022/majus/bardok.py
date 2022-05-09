"""
05-13 F betűs sorok A Walesi bárdokból
Feladat leírás:
Töltsd le és olvasd be A Walesi bárdok c. verset a 'wales.txt' utf-8 kódolású mellékelt fájlból - lásd alább a feladat leírása után.
Írd ki egy "Walesi-bardok-F.txt" fájlba csak azokat a sorokat, amelyekben van kis vagy nagy "f" betű.
A második "végeredmény minta" a létrehozott új fájl tartalmából mutat egy részt.
A mellékelt fájlt innen töltheted le.
"""
path = "magyar-koltok-irok.txt"
file = open(path, "r", encoding="utf-8")
fdata = file.read()
# print(fdata)
fdata = fdata.splitlines()

