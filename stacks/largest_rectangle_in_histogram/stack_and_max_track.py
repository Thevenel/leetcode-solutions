class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # pair (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
    
# Example usage:
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(solution.largestRectangleArea([2,4]))              # Output: 4
print(solution.largestRectangleArea([6,2,5,4,5,1,6]))      # Output: 12 