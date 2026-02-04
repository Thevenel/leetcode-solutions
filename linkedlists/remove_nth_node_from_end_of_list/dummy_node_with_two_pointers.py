from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next
# Example usage:
solution = Solution()
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
new_head = solution.removeNthFromEnd(head, n)
# Printing modified linked list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
print("None")
# Output: 1 -> 2 -> 3 -> 5 -> None
