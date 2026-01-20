class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
       self.stack.append(val)
       val = min(val, self.stack[-1] if self.min_stack else val)
       self.min_stack.append(val)
       
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.getMin())   # Output: -2
min_stack.push(1)
print(min_stack.getMin())   # Output: -2
min_stack.push(-1)
print(min_stack.getMin())   # Output: -2
min_stack.push(-4)
print(min_stack.getMin())   # Output: -4
min_stack.pop()
print(min_stack.getMin())   # Output: -2
