class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                current_area = min(heights[i], heights[j]) * (j - i)
                print("j:", j)
                print("i", i)
                print("j - 1:",  j - 1)
                max_area = max(current_area, max_area)
                
        return max_area

heights = [1,8,6,2,5,4,8,3,7]
csl = Solution()
print(csl.maxArea(heights))