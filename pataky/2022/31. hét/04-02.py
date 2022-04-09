
print('Egy véletlenszerű számokból álló lista elemiről írunk ki információkat.')

itemCount = 5

from random import randint 

data = []

for i in range(itemCount):
 
    newItem = randint(1, 20)

    data.append(newItem)

print("A 'data' lista tartalma: ", data)

print('Lista elemeinek a száma: ',max(data))
print('Lista első eleme: ',data[0])
print('Lista utolsó előtti eleme: ',data[-2])
print('Az első és az utolsó előtti elem szorzata: ',data[0] * data[-2])
print('A lista második és harmadik tagjának különbsége: ',data[1] - data[2])
print('A lista legkisseb elemének duplája: ',min(data) *2)
print('A lista elemeinek összege: ',sum(data))
print('A lista elemeinek átlaga: ',sum(data) / len(data))