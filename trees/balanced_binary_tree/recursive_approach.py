from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[0], right[0])]
        return dfs(root)[0]
# Usage example:
solution = Solution()
# Creating a balanced binary tree: # 1 # / \ # 2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(solution.isBalanced(root))# Output: True