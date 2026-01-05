class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                vals = board[r][c]
                if vals == ".":
                    continue

                sq = (r // 3) * 3 + (c // 3)

                if (vals in rows[r]) or (vals in cols[c]) or (vals in squares[sq]):
                        return False

                cols[c].add(vals)
                rows[r].add(vals)
                squares[sq].add(vals)

        return True



board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"] ]
csl = Solution()
print(csl.isValidSudoku(board))

