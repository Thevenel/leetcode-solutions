class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        list_sorted = sorted(nums)
        n = len(list_sorted)
        for i in range(1, n):
            if list_sorted[i] == list_sorted[i - 1]:
                return True
        return False
    

nums = [1, 2, 3, 1]
csl = Solution()
print(csl.has_duplicate(nums))