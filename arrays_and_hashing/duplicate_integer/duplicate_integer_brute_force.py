class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
nums = [1, 2, 3, 1]
csl = Solution()
print(csl.has_duplicate(nums))
