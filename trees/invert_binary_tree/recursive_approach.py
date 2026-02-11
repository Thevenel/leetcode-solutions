from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Usage example:
solution = Solution()
# Creating a binary tree:
#     4
#    / \
#   2   7
#  / \   \
# 1   3   9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)  

inverted_root = solution.invertTree(root)
# The inverted tree should be:
#     4
#    / \
#   7   2
#  /   / \
# 9   3   1
def print_tree(node):
    if node:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)
        
print_tree(inverted_root)  # Output should reflect the inverted tree structure.
