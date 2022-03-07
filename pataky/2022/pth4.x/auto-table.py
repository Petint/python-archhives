class Table:
    def __init__(self, table_data: 'list[list]'):
        self.tabledata = table_data

    def getfirstrow(self) -> str:
        firstrow = '┌─'
        for __i in range(len(self.tabledata) - 1):
            firstrow += '┬─'
        firstrow += '┐\n'
        return firstrow

    def getrow(self, index: int) -> str:
        row = ''
        for __i in range(len(self.tabledata[index])):
            row += f'│{__i}'
        row += '│\n'
        return row

    def getlastrow(self) -> str:
        lastrow = '└─'
        for __i in range(len(self.tabledata) - 1):
            lastrow += '┴─'
        lastrow += '┘\n'
        return lastrow

    def getseprow(self) -> str:
        seprow = '├─'
        for __i in range(len(self.tabledata) - 1):
            seprow += '┼─'
        seprow += '┤\n'
        return seprow

    def make(self) -> str:
        str_table = ''
        str_table += self.getfirstrow()
        for x in range(len(self.tabledata)):
            str_table += self.getrow(x)
            str_table += self.getseprow()
        str_table += self.getlastrow()
        return str_table


if __name__ == "__main__":
    test_data = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    table1 = Table(test_data)
    print(table1.make())
