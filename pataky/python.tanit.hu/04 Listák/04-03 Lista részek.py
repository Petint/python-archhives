"""
Tölts fel egy 100 elemű listát háromjegyű véletlen egész számokkal és írasd ki
- a tizedik elemét
- a másodiktól az ötödik eleméig
- az utolsó előtti elemét
- az első három elemét
- az utolsó három elemét
- a hetedik elemétől a végéig
"""
from random import randint

print('Egy véletlenszerű háromjegyű egész számokból álló 100 tagú lista külömböző elemeit írjuk ki.')
length_of_list = 100
data = [randint(100, 999) for _ in range(length_of_list)]
print(f"""
A lista tizedik eleme: {data[9]}
A lista másodiktol ötödik elemei : {data[1:5]}
A lista utolsó előtti eleme : {data[-2]}
A lista első három eleme: {data[:3]}
A lista utolsó három eleme: {data[-3:]}
A lista kilencnenhetedik elemétől a végéig: {data[95:-1]}
""")