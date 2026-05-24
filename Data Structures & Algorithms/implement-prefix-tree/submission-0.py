class Node:
    def __init__(self, is_word: bool = False):
        self.is_word = is_word
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.nodes = Node()

    def insert(self, word: str) -> None:
        current = self.nodes
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.nodes
        for ch in word:
            if ch not in current.children:
                return False
            current = current[ch].children
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.nodes
        for ch in word:
            if ch not in current.children:
                return False
            current = current[ch].children
        return True
        