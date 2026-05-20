# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        """
                slow
                  V
        0 -> 1 -> 2 -> 3
                           ^
                          fast
        """

        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        """
        prev = None
                
        0 -> 1 -> 2 <-- 3        
                  |     ^         
                  V   prev     
                 None
        """

        """
       
      head
        0 -> 1 -> 2 <-- 3        
                  |     ^         
                  V    tail
                 None
        """
        current_head = head
        current_tail = prev
        while current_head.next and current_tail.next:
            next_head = current_head.next
            current_head.next = current_tail
            current_head = next_head
            next_tail = current_tail.next
            current_tail.next = current_head
            current_tail = next_tail