class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sm = 0
        mx = 0
        id = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            sm += diff
            mx += diff
            if mx < 0:
                id = i + 1
                mx = 0
        
        if sm >= 0:
            return id
        else:
            return -1