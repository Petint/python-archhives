from random import randint

l_o_l = 100
data = [randint(100, 999) for _ in range(l_o_l)]
print(f"""
A lista tizedik eleme: {data[9]}
A lista másodiktol ötödik elemei : {data[1:5]}
A lista utolsó előtti eleme : {data[-2]}
A lista első három eleme: {data[:3]}
A lista utolsó három eleme: {data[-3:]}
A lista kilencnenhetedik elemétől a végéig: {data[95:-1]}
""")