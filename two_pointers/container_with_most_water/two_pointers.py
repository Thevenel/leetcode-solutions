class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1
        while l < r:
            current_area = (r - l) * min(height[l], height[r])
            max_area = max(current_area, max_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

heights = [1,8,6,2,5,4,8,3,7]
csl = Solution()
print(csl.maxArea(heights))