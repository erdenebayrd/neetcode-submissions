"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copied = {}
        current = head
        while current:
            copied[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copied[current].random = copied.get(current.random)
            copied[current].next = copied.get(current.next)
            current = current.next
        return copied[head]