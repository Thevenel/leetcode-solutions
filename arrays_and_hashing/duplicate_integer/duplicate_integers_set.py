class Solution:
    def has_duplicate(self, nums:list[int])-> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

nums = [1, 2, 3, 4]

csl = Solution()
print(csl.has_duplicate(nums))
