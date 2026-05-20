from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1
        
        n = len(nums)
        frequency = [[] for _ in range(n + 1)]
        for num in counter:
            frequency[counter[num]].append(num)
        
        result = []
        for count in range(n, 0, -1):
            if len(frequency[count]) == 0 or k == 0:
                continue
            result.extend(frequency[count])
            k -= len(frequency[count])
        return result