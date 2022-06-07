from autotable import Table

size = 25
test_data = [[x * size + y for y in range(size)] for x in range(size)]
table1 = Table(test_data, length=5, align='c')
with open("table.txt", "w") as f:
    f.write(table1.make())
