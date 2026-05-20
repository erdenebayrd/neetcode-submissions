from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupIndices = defaultdict(list)
        for i in range(len(strs)):
            current = strs[i]
            counter = defaultdict(int)
            for ch in current:
                counter[ch] += 1
            key = ""
            for ch in counter:
                print(ch, counter[ch])
            print(key)
        