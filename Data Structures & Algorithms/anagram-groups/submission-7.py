from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in range(len(strs)):
            counter = [0] * 26
            for ch in strs[i]:
                counter[ord(ch) - ord('a')] += 1
            result[tuple(counter)].append(strs[i])
        
        return list(result.values())