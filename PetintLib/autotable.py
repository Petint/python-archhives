class Table:
    """Easy way of making unicode tables"""

    def __init__(self, table_data: 'list[list]', length: int = 5):
        self._t1 = __Table__(table_data, length)

    def make(self) -> str:
        """
        Generates the table string.
        Desinged to be passed to print() i.e. print(table1.make())
        usage:
            1. Turn list into table: able1 = Table[data]
            2. print the table :     print(table1.make())
        """
        return self._t1.make()


class __Table__:
    """
    Internal class
    Use facade pls
    """

    def __init__(self, table_data: 'list[list]', length: int):
        self.tabledata = table_data
        self.item_length = length

    def getfirstrow(self) -> str:
        firstrow = '┌'
        firstrow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            firstrow += '┬'
            firstrow += self.item_length * "─"
        firstrow += '┐\n'
        return firstrow

    def getrow(self, index: int) -> str:
        row = ''
        for __i in range(len(self.tabledata[index])):
            row += '│'
            row += f'{self.tabledata[index][__i]}'
            if len(str(self.tabledata[index][__i])) < self.item_length:
                row += (self.item_length - len(str(self.tabledata[index][__i]))) * " "
        row += '│\n'
        return row

    def getlastrow(self) -> str:
        lastrow = '└'
        lastrow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            lastrow += '┴'
            lastrow += self.item_length * "─"
        lastrow += '┘\n'
        return lastrow

    def getseprow(self) -> str:
        seprow = '├'
        seprow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            seprow += '┼'
            seprow += self.item_length * "─"
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
