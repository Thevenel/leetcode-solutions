class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

numbers = [2, 7, 11, 15]
target = 9
csl = Solution()
print(csl.twoSum(numbers, target))