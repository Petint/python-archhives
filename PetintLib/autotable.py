class Table:
    def __init__(self, table_data: 'list[list]'):
        self.tabledata = table_data

    def getfirstrow(self) -> str:
        firstrow = '┌───'
        for __i in range(len(self.tabledata[0]) - 1):
            firstrow += '┬───'
        firstrow += '┐\n'
        return firstrow

    def getrow(self, index: int) -> str:
        row = ''
        for __i in range(len(self.tabledata[index])):
            row += '│'
            if len(str(self.tabledata[index][__i])) < 3:
                row += " "
            row += f'{self.tabledata[index][__i]}'
            if len(str(self.tabledata[index][__i])) < 2:
                row += " "
        row += '│\n'
        return row

    def getlastrow(self) -> str:
        lastrow = '└───'
        for __i in range(len(self.tabledata[0]) - 1):
            lastrow += '┴───'
        lastrow += '┘\n'
        return lastrow

    def getseprow(self) -> str:
        seprow = '├───'
        for __i in range(len(self.tabledata[0]) - 1):
            seprow += '┼───'
        seprow += '┤\n'
        return seprow

    def make(self) -> str:
        str_table = ''
        str_table += self.getfirstrow()
        for x in range(len(self.tabledata)):
            str_table += self.getrow(x)
            if x < len(self.tabledata) - 1:
                str_table += self.getseprow()
        str_table += self.getlastrow()
        return str_table


if __name__ == "__main__":
    size = 30
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    table1 = Table(test_data)
    print(table1.make())
