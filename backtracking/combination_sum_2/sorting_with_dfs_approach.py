from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        
        return res 
    
# Usage
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))  # Output: [[1,2,2], [5]]