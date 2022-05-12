path = "eredmeny.txt"
file = open(path, 'r')
text = file.read()
file.close()
lista = text.splitlines()
arraym = [i.split(';') for i in lista]
print(arraym)
