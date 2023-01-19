"""
05-02
Olvasd be a 'magyar-koltok-irok.txt' utf-8 kódolású szövegfájl tartalmát és írd ki a konzolra a költőket.
"""

path = "koltok.txt"
with open(path, 'rt', encoding="utf-8") as koltok_file:
    koltok_file_data = koltok_file.read()
koltok = koltok_file_data.splitlines()
for k in koltok:
    if 'költő' in k.lower():
        print(k)
