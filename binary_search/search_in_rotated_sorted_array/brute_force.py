class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    

# Example usage:
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(solution.search([1], 0))              # Output: -1