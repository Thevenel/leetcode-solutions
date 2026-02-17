class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# Usage
# Constructing the binary tree
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9   
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


# Finding the lowest common ancestor of nodes 2 and 8
solution = Solution()
lca = solution.lowestCommonAncestor(root, root.left, root.right)
print(f"The lowest common ancestor of nodes 2 and 8 is: {lca.val}") 