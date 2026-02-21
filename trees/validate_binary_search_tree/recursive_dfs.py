from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
# Usage
# Constructing a binary tree
#         2
#        / \
#       1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
is_valid_bst = solution.isValidBST(root)
print(f"The binary tree is a valid binary search tree: {is_valid_bst}")

