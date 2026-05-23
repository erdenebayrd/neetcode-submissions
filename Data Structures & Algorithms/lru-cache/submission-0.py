from typing import Optional

class Node:
    def __init__(self, key: str, value: int = 0, prev: Optional[Node] = None, next: Optional[Node] = None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append_right(self, node: Node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        self.tail.prev = node
        node.next = self.tail
        self.size += 1
    
    def pop_left(self) -> Node:
        deleted_node = self.head.next
        self.head.next = deleted_node.next
        deleted_node.next.prev = self.head
        deleted_node.next = deleted_node.prev = None
        self.size -= 1
        return deleted_node
    
    def delete(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        value = node.value
        self.linked_list.delete(node)
        self.linked_list.append_right(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes: # append right
            node = Node(key=key, value=value)
            self.nodes[key] = node
            self.linked_list.append_right(node)
            if self.linked_list.size and self.linked_list.size > self.capacity:
                deleted_node = self.linked_list.pop_left()
                del self.nodes[deleted_node.key]
        else:    
            node = self.nodes[key]
            self.linked_list.delete(node)
            self.linked_list.append_right(node)



