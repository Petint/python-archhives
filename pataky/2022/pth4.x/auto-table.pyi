class Table:
    tableParts = '─│└┘├┤┴┼'
    def __init__(self,table_data: 'list[list]'):
        self.tabledata = table_data

    def getfirstrow(self):
        firstrow = '┌─'
        for __i in range(len(self.tabledata)):
            firstrow += '┬─'
        firstrow += '┐'
        return firstrow

    def make(self) -> str:
        firstRow = self.getfirstrow()

