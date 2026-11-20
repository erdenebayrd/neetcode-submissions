from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # # time: O(n log n)
        # # space: O(n)
        # # method: sorting + count

        n = len(hand)
        if n % groupSize != 0:
            return False
        
        # hand.sort()
        # count = Counter(hand)
        # for start_candidate in hand:
        #     if count[start_candidate] == 0:
        #         continue
        #     for i in range(start_candidate, start_candidate + groupSize):
        #         if count[i] <= 0:
        #             return False
        #         count[i] -= 1
        # return True

        # time: O(n + max(hand) - min(hand))

        count = Counter(hand)
        for value in range(min(hand), max(hand) + 1):
            if count[value] == 0:
                continue
            for i in range(value, value + groupSize):
                if count[i] <= 0:
                    return False
                count[i] -= 1
        return True