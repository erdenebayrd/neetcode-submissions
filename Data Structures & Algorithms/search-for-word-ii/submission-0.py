class Node:
    def __init__(self) -> None:
        self.children = {}
        self.indices = [] # word indices of the given words list

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def add(self, word: str, index: int) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.indices.append(index)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # time: O(rows * cols * 3 ^ max(len(words[i])) + sum(len(words[i])))
        # space: O(sum(len(words[i])))
        # method: Trie + backtrack
        rows = len(board)
        cols = len(board[0])

        trie = Trie()
        for i in range(len(words)):
            trie.add(words[i], i)

        found = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def backtrack(row: int, col: int, node: "Node") -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in seen or board[row][col] not in node.children:
                return
            seen.add((row, col))
            node = node.children[board[row][col]]
            for index in node.indices:
                found.add(index)

            for delta_row, delta_col in directions:
                next_row, next_col = delta_row + row, delta_col + col
                backtrack(next_row, next_col, node)
            
            seen.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                seen = set()
                backtrack(row, col, trie.root)

        result = []
        for index in found:
            result.append(words[index])
        return result