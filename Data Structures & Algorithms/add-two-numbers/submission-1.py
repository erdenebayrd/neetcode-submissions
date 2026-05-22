# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        current = result
        while l1 or l2 or carry:
            value1 = value2 = 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next
            value = value1 + value2 + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
        
        return result.next