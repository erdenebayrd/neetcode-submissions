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
        # space: O(n)
        # method: count

        # count = Counter(hand)
        # for value in range(min(hand), max(hand) + 1):
        #     while count[value]:
        #         for i in range(value, value + groupSize):
        #             if count[i] <= 0:
        #                 return False
        #             count[i] -= 1
        # return True
        # time: O(n)
        # space: O(n)
        # method: Greedy
        count = Counter(hand)
        for number in hand:
            start = number
            while count[start - 1]:
                start -= 1
            
            while start <= number:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if count[i] <= 0:
                            return False
                        count[i] -= 1
                start += 1
        return True