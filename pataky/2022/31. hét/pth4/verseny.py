path = "eredmeny.txt"
file = open(path, 'r')
text = file.read()
file.close()
lista = text.splitlines()
arraym = [l.split(';') for l in lista]
print(arraym)
