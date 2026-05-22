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
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value = l1.val + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            l1 = l1.next

        while l2:
            value = l2.val + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            l2 = l2.next

        while carry:
            value = carry % 10
            carry //= 10
            current.next = ListNode(value)
            current = current.next
        
        return result.next