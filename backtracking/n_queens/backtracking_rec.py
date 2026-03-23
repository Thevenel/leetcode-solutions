class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
# Usage Example
solution = Solution()
n = 4
result = solution.solveNQueens(n)
for board in result:    
    for row in board:
        print(row)
        print()
# Output:
# .Q..
# ...Q
# Q...
# ..Q.
# ..Q.
# Q...
# ...Q
# .Q..
