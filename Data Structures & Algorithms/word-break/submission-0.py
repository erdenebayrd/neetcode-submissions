from functools import cache

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def add(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time: O(N ^ 2 + M) N is len of s
        # space: O(N + M) M is total number of chars in wordDict
        # method: Trie + DP

        trie = Trie()
        n = len(s)
        for word in wordDict:
            trie.add(word)
        
        @cache
        def solve(index: int) -> bool:
            if index >= n:
                return True
            
            current_node = trie.root
            
            result = False
            for i in range(index, n):
                ch = s[i]
                if ch not in current_node.children or result:
                    return result
                current_node = current_node.children[ch]
                if current_node.is_word:
                    result |= solve(i + 1)
                
            return result
        
        return solve(0)