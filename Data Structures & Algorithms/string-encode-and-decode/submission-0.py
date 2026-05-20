class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + ":" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            indexDelimeter = index
            while indexDelimeter < len(s) and s[indexDelimeter] != ":":
                indexDelimeter += 1
            length = int(s[index:indexDelimeter]) # not including right index
            result.append(s[indexDelimeter + 1:indexDelimeter + length + 1])
            index = indexDelimeter + length + 1
        return result