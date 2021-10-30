"""
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    # Check if the board is valid
    if not isValid(board):
        return False

    # Check if the board is solved
    if isSolved(board):
        return True

    # Find the first empty cell
    row, col = findEmptyCell(board)

    # Try all possible values
    for i in range(1, 10):
        board[row][col] = str(i)
        if solveSudoku(board):
            return True
        board[row][col] = '.'

    return False

def isSolved(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check if the board is solved
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return False

    return True

def findEmptyCell(board):
    """
    :type board: List[List[str]]
    :rtype: (int, int)
    """
    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j

def isValid(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check if the board is valid
    for i in range(9):
        # Check if each row is valid
        if not isValidRow(board, i):
            return False

        # Check if each column is valid
        if not isValidCol(board, i):
            return False

        # Check if each 3x3 sub-box is valid
        if not isValidSubBox(board, i):
            return False

    return True

def isValidRow(board, row):
    """
    :type board: List[List[str]]
    :type row: int
    :rtype: bool
    """
    # Check if each row is valid
    row_set = set()
    for i in range(9):
        if board[row][i] in row_set:
            return False
        row_set.add(board[row][i])

    return True

def isValidCol(board, col):
    """
    :type board: List[List[str]]
    :type col: int
    :rtype: bool
    """
    # Check if each column is valid
    col_set = set()
    for i in range(9):
        if board[i][col] in col_set:
            return False
        col_set.add(board[i][col])

    return True

def isValidSubBox(board, row):
    """
    :type board: List[List[str]]
    :type row: int
    :rtype: bool
    """
    # Check if each 3x3 sub-box is valid
    sub_box_set = set()
    for i in range(3):
        for j in range(3):
            if board[row][i] in sub_box_set:
                return False
            sub_box_set.add(board[row][i])

    return True