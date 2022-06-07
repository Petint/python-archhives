class Table:
    """Easy way of making unicode tables"""

    def __init__(self, table_data: 'list[list]', length: int = 0, align: chr = 'w'):
        """
            table_data: 'list[list[any]]' - Data for the table

            length: int - Width of a cell, auto by default

            align: str - 'w' for west, 'e' - for east, 'c' - for center (west by default, center is kinda iffy.)
        """
        if length == 0:
            length = auto(table_data)
        self._t1 = TableInternal(table_data, length, align)

    def make(self) -> str:
        """
        Generates the table.
        Returns string
        usage:
            1. Turn list into table: table1 = Table(data)
            2. print the table :     print(table1.make())
        """
        return self._t1.make()


class TableInternal:
    """
    Internal class
    Use facade pls
    """

    def __init__(self, table_data: 'list[list]', length: int, align: chr):
        self.tabledata = table_data
        self.item_length = length
        self.align = align.lower()

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
            loclen = len(str(self.tabledata[index][__i]))
            diff = self.item_length - loclen
            row += '│'
            if self.align == 'w':  # Align west
                row += f'{self.tabledata[index][__i]}' + diff * " "
            elif self.align == 'e':  # Align east
                row += diff * " " + f'{self.tabledata[index][__i]}'
            elif self.align == 'c':  # Align center /// Credit goes to KillerCat#7249
                half = diff / 2
                mg = int(half) * " "  # margin
                if int(half) == half:
                    row += mg + f'{self.tabledata[index][__i]}' + mg
                else:
                    row += mg + "  " f'{self.tabledata[index][__i]}' + " " + mg
                    # row += mg + "\t" f'{self.tabledata[index][__i]}' +  mg
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
        str_table += self.getfirstrow()  # Head
        sepr = self.getseprow()  # Separator row
        for x in range(len(self.tabledata)):  # Main content
            str_table += self.getrow(x)
            if x < len(self.tabledata) - 1:
                str_table += sepr
        str_table += self.getlastrow()  # Footer
        return str_table


def auto(data: 'list[list]') -> int:
    """Finds the longest entry and returns its length."""
    lengths = []
    for i in data:
        for j in i:
            lengths.append(len(str(j)))
    return max(lengths)
