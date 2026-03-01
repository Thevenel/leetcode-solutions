from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
    