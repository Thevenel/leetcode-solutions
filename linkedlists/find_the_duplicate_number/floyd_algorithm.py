from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow2 == slow:
                return slow
            
# Usage example:
solution = Solution()
nums = [1, 3, 4, 2, 2]
duplicate = solution.findDuplicate(nums)
print(f"The duplicate number is: {duplicate}")  # Output: The duplicate number is: 2
