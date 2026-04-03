class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)
        x = 1
        for i in range(1,n+1):
            if x*2 == i:
                x = i
            output[i] = 1 + output[i - x]
        return output