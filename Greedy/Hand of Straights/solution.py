class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        n = len(hand) // groupSize
        counts = dict.fromkeys(hand, 0)
        for value in hand:
            counts[value] += 1

        for _ in range(n):
            min_value = min(counts.keys())

            for i in range(groupSize):
                if (min_value + i) not in counts:
                    return False
                counts[min_value + i] -= 1
                if counts[min_value + i] == 0:
                    del counts[min_value + i]
            
        return True


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        n = len(hand) // groupSize
        counts = dict.fromkeys(hand, 0)
        for value in hand:
            counts[value] += 1

        for _ in range(n):
            min_value = min(counts.keys())

            for value in range(min_value, min_value + groupSize):
                if value not in counts:
                    return False
                counts[value] -= 1
                if counts[value] == 0:
                    del counts[value]
            
        return True


from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        n = len(hand) // groupSize
        counts = Counter(hand)

        for _ in range(n):
            min_value = min(counts.keys())

            for value in range(min_value, min_value + groupSize):
                if value not in counts:
                    return False
                counts[value] -= 1
                if counts[value] == 0:
                    del counts[value]
            
        return True


