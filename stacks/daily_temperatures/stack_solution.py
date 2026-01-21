class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                result[stack_ind] = (i - stack_ind)
            stack.append([t, i])
        return result
    
# Example usage:
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([30,40,50,60]))              # Output: [1,1,1,0]
print(solution.dailyTemperatures([30,60,90]))                 # Output: [1,1,0]
print(solution.dailyTemperatures([90,80,70,60]))              # Output: [0,0,0,0]
print(solution.dailyTemperatures([55,56,57,58,59,60,61]))      # Output: [1,1,1,1,1,1,0]