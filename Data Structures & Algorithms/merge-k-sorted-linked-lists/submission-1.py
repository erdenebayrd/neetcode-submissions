# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        while any(lists):
            min_head = None
            min_index = -1
            for index, head in enumerate(lists):
                if not head:
                    continue
                if not min_head or min_head.val > head.val:
                    min_head = head
                    min_index = index
            
            current.next = min_head
            current = current.next
            lists[min_index] = lists[min_index].next
        return result.next