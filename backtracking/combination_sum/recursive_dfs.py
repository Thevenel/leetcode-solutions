from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
# Usage
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(solution.combinationSum([2, 3, 5], 8))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
