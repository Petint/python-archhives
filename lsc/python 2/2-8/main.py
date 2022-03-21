board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def printboard(_board):
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    for i in range(len(_board)):
        for j in range(len(_board[0])):
            print(f"│ {_board[i][j]} ", end="")
        print("│")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")


def fempty(_board):
    for i in range(len(_board)):
        for j in range(len(_board[0])):
            if _board[i][j] == 0:
                return i, j
    return None


def valid(_board, num, pos):
    for i in range(len(_board)):
        if _board[pos[0]][i] == num and pos[1] != i:
            return not True
    for i in range(len(_board)):
        if _board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x, box_y = pos[1] // 3, pos[0] //3
    for i in range(box_y * 3 ,box_y * 3 + 3):
        for j in range(box_x * 3 ,box_x * 3 + 3):
            if _board[i][j] == num and pos[0] != i:
                return False
    return True


def solve(_board):
    find = fempty(_board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(_board, i, (row, col)):
            _board[row][col] = i
            if solve(_board):
                return True
            _board[row][col] = 0
    return False


printboard(board)
solve(board)
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
printboard(board)
