from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
# Example usage:
solution = Solution()
# Creating a linked list with a cycle for testing
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle here
print(solution.hasCycle(node1))  # Output: True
# Creating a linked list without a cycle for testing
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeA.next = nodeB
print(solution.hasCycle(nodeA))  # Output: False
print(solution.hasCycle(None))    # Output: False
