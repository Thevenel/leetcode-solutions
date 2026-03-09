from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]
        for n in nums:
            new_perm = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perm.append(p_copy)
            perms = new_perm
        return perms
        


# Usage
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(solution.permute([0, 1]))  # Output: [[0, 1], [1, 0]]
print(solution.permute([1]))  # Output: [[1]]