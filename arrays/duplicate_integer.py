class Solution:
    def has_duplicate(self, nums:list[int])-> bool:
        for i in range(len(nums) -1):
            if nums[i] == nums[i + 1]:
                return True
        return False

nums = [1, 2, 3, 4]

csl = Solution()
print(csl.has_duplicate(nums))
