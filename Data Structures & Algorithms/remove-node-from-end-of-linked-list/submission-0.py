# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        k = length - n
        if k == 0:
            return head.next
        
        prev = None
        current = head
        while k:
            k -= 1
            prev = current
            current = current.next
        prev.next = current.next
        return head