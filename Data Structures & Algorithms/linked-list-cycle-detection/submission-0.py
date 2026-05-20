# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        turtle = head
        rabbit = head.next
        while turtle and rabbit.next:
            turtle = turtle.next
            rabbit.next.next
            if turtle == rabbit:
                return True
        return False