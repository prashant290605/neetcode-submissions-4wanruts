class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets:
            return False

        a,b,c = 0,0,0
        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                if i[0] == target[0]:
                    a = 1
                if i[1] == target[1]:
                    b = 1
                if i[2] == target[2]:
                    c = 1
        return [a,b,c] == [1,1,1]