def printiger(p):
    for x in range(p+1):
        print(x, end=" ")


printiger(123)


def matrix_sum(data: 'list[list[int]]') -> int:
    total = 0
    for i in data:
        for p in i:
            total += p
    return total


matrix = [[x+y for y in range(5)] for x in range(5)]
print('\n\n', matrix, matrix_sum(matrix), sep="\n")

