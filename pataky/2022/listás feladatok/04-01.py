data = [3, 45, 6, 8, 324, 56, 23, 45, 98, 777, 678, 83, 65, 98]

print(f"""
Egy előre meghatárorott lista elemeiről írunk ki információkat.
A lista {len(data)} elemet tartalmaz.
A lista első eleme: {data[0]}
A lista utolsó eleme: {data[-1]}
A lista harmadik és ötödik elemének összege: {data[2] + data[4]}
A lista legkisebb éretéke: {min(data)}
A lista legnagyobb értéke: {max(data)}
A lista elemeinek az összege: {sum(data)}
A lista elemeinek az átlaga: {sum(data) / len(data)}
""")