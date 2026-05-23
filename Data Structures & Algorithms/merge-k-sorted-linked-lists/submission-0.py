import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        min_heap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            head = lists[i]
            heapq.heappush(min_heap, (head.val, i, head))

        # [1, 2, 4]
        # [1, 3, 5]
        # [3, 6]
        
        # {1, 3}
        # [1, ]

        while min_heap:
            _, tie_breaker, head = heapq.heappop(min_heap)
            if head.next:
                heapq.heappush(min_heap, (head.next.val, tie_breaker, head.next))
            current.next = head
            current = current.next
            
        return result.next