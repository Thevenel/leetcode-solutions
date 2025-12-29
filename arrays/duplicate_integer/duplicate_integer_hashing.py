class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = 1

        return False

nums = [1, 2, 3, 1, 5, 6, 3]
csl = Solution()
print(csl.has_duplicate(nums))
