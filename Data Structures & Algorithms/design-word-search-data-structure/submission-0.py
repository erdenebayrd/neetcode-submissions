class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()  

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.is_word = True

    def __search(self, index: int, word: str, node: "Node") -> bool:
        if index >= len(word):
            return node.is_word
        
        ch = word[index]
        if ch == ".":
            for child in node.children:
                if self.__search(index + 1, word, node.children[child]):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.__search(index + 1, word, node.children[ch])

    def search(self, word: str) -> bool:
        return self.__search(0, word, self.root)