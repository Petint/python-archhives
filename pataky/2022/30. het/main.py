"""File handling"""

# 05-01
"""
Olvasd be a 'magyar-koltok-irok.txt' utf-8 kódolású szövegfájl tartalmát és írd azt ki a konzolra.
"""

path = "koltok.txt"
koltok_file = open(path, 'rt', encoding="utf-8")
koltok_file_data = koltok_file.read()
koltok_file.close()
print(koltok_file_data)
