class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # method: greedy

        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        start_index = 0
        total = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start_index = i + 1
        return start_index