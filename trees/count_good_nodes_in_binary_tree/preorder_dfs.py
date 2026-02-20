class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            
            if not node:
                return 0
            
            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        return dfs(root, root.val)
# Usage example:
# Constructing a binary tree:
#         3
#        / \
#       1   4
#      /   / \
#     3   1   5
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5) 
solution = Solution()
result = solution.goodNodes(root)
print(f"The number of good nodes in the binary tree is: {result}")

