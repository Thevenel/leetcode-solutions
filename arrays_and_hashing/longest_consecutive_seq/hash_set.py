class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

nums = [100, 4, 200, 1, 3, 2]
csl = Solution()
print(csl.longestConsecutive(nums))
