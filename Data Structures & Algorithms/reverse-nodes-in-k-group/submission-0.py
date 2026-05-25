from typing import Tuple
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        def reverse_group(head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]: # head and tail (reversed)
            prev = None
            current = head
            end_node = tail.next
            while current != end_node:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return (tail, head)

        counter = 0
        current = head
        result = ListNode()
        result.next = head
        prev_head = result
        group_head = group_tail = None

        while current:
            next_current = current.next
            if counter == 0:
                group_head = current
            elif counter == k - 1:
                group_tail = current
                group_head, group_tail = reverse_group(group_head, group_tail)
                group_tail.next = next_current
                prev_head.next = group_head
                prev_head = group_tail

            counter = (counter + 1) % k
            current = next_current

        return result.next
