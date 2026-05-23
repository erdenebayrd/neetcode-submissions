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
            min_index = -1
            for index, head in enumerate(lists):
                if not head:
                    continue
                if min_index == -1 or lists[min_index].val > head.val:
                    min_index = index
            
            current.next = lists[min_index]
            current = current.next
            lists[min_index] = lists[min_index].next
        return result.next