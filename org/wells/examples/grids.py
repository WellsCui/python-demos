# Given a matrix of n*n size, the task is to print its elements in diagonally pattern.

# Input : mat[3][3] = {{1, 2, 3},
#                      {4, 5, 6},
#                      {7, 8, 9}}
# Output : 1 2 4 7 5 3 6 8 9.
# Explanation: We start from 1
# Then from upward to downward diagonally i.e. 2 and 4
# Then from downward to upward diagonally i.e 7,5,3
# Then from up to down diagonally i.e  6, 8
# Then down to up i.e. end at 9.
#
# Input : mat[4][4] =  {{1,  2,  3,  10},
#                       {4,  5,  6,  11},
#                       {7,  8,  9,  12},
#                       {13, 14, 15, 16}}
# Output:  1 2 4 7 5 3 10 6 8 13 14 9 11 12 15 16 .

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def equals(self, pos):
        return self.row == pos.row and self.col == pos.col


def output_matrix_elements_in_diagonal(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    def get_points(start, end, row_step, col_step):
        rs = []
        current = start
        while not current.equals(end):
            current = Position(current.row + row_step, current.col + col_step)
            rs.append(current)
        return rs

    current = Position(0, 0)
    end = Position(row_size - 1, col_size - 1)
    result = [current]

    while True:
        if current.row == 0 and current.col < col_size - 1:
            current = Position(current.row, current.col + 1)
        else:
            current = Position(current.row + 1, current.col)
        result.append(current)
        points = get_points(current, Position(current.col, current.row), 1, -1)
        result += points
        current = points[-1]

        if current.col == 0 and current.row < row_size - 1:
            current = Position(current.row + 1, current.col)
        else:
            current = Position(current.row, current.col + 1)

        result.append(current)
        if current.equals(end):
            break

        points = get_points(current, Position(current.col, current.row), -1, 1)
        result += points
        current = points[-1]

    return result


def run_test():
    matrixes = [[[1, 2],
                 [3, 4]],
                [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],
                [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]]

    for item in matrixes:
        print([item[pos.row][pos.col] for pos in output_matrix_elements_in_diagonal(item)])


run_test()


# Gold Mine Problem
# 2.4
# Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in
# tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\)
# that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down
# towards the right. Find out maximum amount of gold he can collect.

# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                    {0, 6, 4}};
# Output : 12
# {(1,0)->(2,1)->(2,2)}
#
# Input: mat[][] = { {1, 3, 1, 5},
#                    {2, 2, 4, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 1, 2}};
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)
#
# Input : mat[][] = {{10, 33, 13, 15},
#                    {22, 21, 04, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 14, 2}};
# Output : 83

def mine_gold(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    def mine(row, col):
        if col >= col_size:
            return 0
        right_mine = mine(row, col + 1)
        up_right_mine = 0 if row == 0 else mine(row - 1, col + 1)
        down_right_mine = 0 if row == row_size - 1 else mine(row + 1, col + 1)
        return matrix[row][col] + max(right_mine, up_right_mine, down_right_mine)

    max_mine = 0
    for begin_row in range(row_size):
        result = mine(begin_row, 0)
        max_mine = result if result > max_mine else max_mine
    return max_mine


def mine_test():
    mat = [[1, 3, 1, 5],
           [2, 2, 4, 1],
           [5, 0, 2, 3],
           [0, 6, 1, 2]]
    print(mine_gold(mat))


mine_test()
