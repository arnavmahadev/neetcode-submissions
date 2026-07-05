class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for digit in row:
                if digit == '.':
                    continue
                if digit in rowSet:
                    return False
                rowSet.add(digit)
        for i in range(9):
            colSet = set()
            for x in range(9):
                if board[x][i] == '.':
                    continue
                if board[x][i] in colSet:
                    return False
                colSet.add(board[x][i])
        for i in range(0, 9, 3):
            for x in range(0, 9, 3):
                boxSet = set()
                for c in range(i, i + 3):
                    for r in range(x, x + 3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in boxSet:
                            return False
                        boxSet.add(board[r][c])
        return True