class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
               stack.append(stack.pop() + stack.pop())
            elif c == "-":
               a, b = stack.pop(), stack.pop()
               stack.append(b - a)
            elif c == "*":
               stack.append(stack.pop() * stack.pop())
            elif c == "/":
               a, b = stack.pop(), stack.pop()
               stack.append(int(b / a))
            else:
               stack.append(int(c)) 
               
        return stack[0]
    
# Example usage:
solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))          # Output: 9
print(solution.evalRPN(["4","13","5","/","+"]))         # Output: 6    
print(solution.evalRPN(["3","-4","+"]))                  # Output: -1