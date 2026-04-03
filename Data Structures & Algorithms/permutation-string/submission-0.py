class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        counts1 = {}
        for i in s1:
            counts1[i] = 1 + counts1.get(i,0)
        

        l = 0
        r = n1-1
        while r < len(s2):
            count = {}
            for i in s2[l:r+1]:
                count[i] = 1 + count.get(i,0)
            if count == counts1:
                return True
            else:
                count[s2[l]] -= 1
                l += 1
                r += 1
        return False
