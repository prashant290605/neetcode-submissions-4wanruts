class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ct = Counter(hand)
        hand.sort()
        for num in hand:
            if ct[num]:
                for i in range(num,num+groupSize):
                    if not ct[i]:
                        return False
                    else:
                        ct[i] -= 1
        return True