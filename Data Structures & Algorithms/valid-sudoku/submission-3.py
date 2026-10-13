class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(len(board))}
        cols = {i: set() for i in range(len(board))}
        squares = {i: set() for i in range(len(board))}

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                box = (row // 3) * 3 + (col // 3)
                if val == ".":
                    continue
                elif val in rows[row]:
                    return False
                elif val in cols[col]:
                    return False
                elif val in squares[box]:
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[box].add(val)
        return True


