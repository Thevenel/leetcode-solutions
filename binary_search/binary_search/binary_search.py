class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
# Example usage:
solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))  # Output: 4
print(solution.search([-1,0,3,5,9,12], 2))  # Output: -1
print(solution.search([5], 5))              # Output: 0