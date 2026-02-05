class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        old_to_copy = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[copy.random]
            cur = cur.next

        return old_to_copy[head]
# Usage example:
# Creating a linked list with random pointers
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node1.random = node2
node2.random = node1
solution = Solution()
copied_head = solution.copyRandomList(node1)
# Now copied_head is a deep copy of the original linked list with random pointers.
while copied_head:
    print(f"Node value: {copied_head.val}, Random points to: {copied_head.random.val if copied_head.random else None}")
    copied_head = copied_head.next

