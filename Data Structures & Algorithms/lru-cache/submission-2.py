from typing import Optional

class Node:
    def __init__(self, key: str, value: int = 0, prev: Optional[Node] = None, next: Optional[Node] = None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            new_node = Node(key=key, value=value, prev=self.tail.prev, next=self.tail)
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            self.nodes[key] = new_node
            self.size += 1
            if self.size > self.capacity: # delete leftmost node
                del self.nodes[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                self.size -= 1
        else:
            node = self.nodes[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail.prev
            self.tail.prev.next = node
            node.next = self.tail
            self.tail.prev = node