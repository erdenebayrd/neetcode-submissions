class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # time: O(n) n is len of gas
        # space: O(n)
        # method: SWAG prefix sum

        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        prefix = diff + diff
        for i in range(1, 2 * n):
            prefix[i] += prefix[i - 1]
        

        inf = float('inf')
        left = []
        right = prefix[:n]
        right_min = inf
        
        current = 0
        for i in range(n):
            if not left:
                while right:
                    value = right.pop()
                    if not left:
                        left.append(value)
                    else:
                        left.append(min(left[-1], value))

                right_min = inf
            
            window_min = min(right_min, left[-1])
            right.append(prefix[i + n])
            right_min = min(right_min, right[-1])
            left.pop()

            if current <= window_min:
                return i

            current = prefix[i]
        return -1