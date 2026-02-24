from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            
            res[0] = max(res[0], root.val + left_max + right_max)
            return root.val + max(left_max, right_max)
        dfs(root)
        return res[0]
# Usage example:
# Constructing the binary tree:
#         1
#        / \
#       2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3) 
solution = Solution()
print(solution.maxPathSum(root))  # Output: 6 (path is 2 -> 1 -> 3)
