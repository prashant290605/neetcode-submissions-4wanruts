class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
 

        ct = Counter(hand)
        hand.sort()
        count = 0
        for i in hand:
            if ct[i]:
                for j in range(groupSize):
                    if not ct[i+j]:
                        return False
                    else:
                        ct[i+j] -= 1
        return True