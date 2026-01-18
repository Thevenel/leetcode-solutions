class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_map = {")":"(", "]":"[", "}":"{"}
        
        for c in s:
            if c in braces_map:
                if stack and stack[-1] == braces_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
# Example usage:
solution = Solution()
print(solution.isValid("()"))          # Output: True
print(solution.isValid("()[]{}"))      # Output: True
print(solution.isValid("(]"))          # Output: False
print(solution.isValid("([)]"))        # Output: False
print(solution.isValid("{[]}"))        # Output: True   