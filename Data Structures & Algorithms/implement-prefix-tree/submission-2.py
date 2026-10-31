class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True

