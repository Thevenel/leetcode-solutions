# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
        tail = tail.next
    

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
    
# Example usage:
solution = Solution()
# Creating first sorted linked list: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Creating second sorted linked list: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = solution.mergeTwoLists(list1, list2)
# Printing merged linked list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None