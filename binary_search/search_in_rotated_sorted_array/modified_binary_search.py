class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
        
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target <= nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1 
        return -1


solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(solution.search([1], 0))              # Output: -1