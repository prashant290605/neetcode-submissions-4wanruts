class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        s = str(n)
        while True:
            val = 0
            for i in s:
                j = int(i)
                val += j**2
            if hash and val != 1 and val in hash:
                return False
            if val == 1:
                return True
            else:
                s = str(val)
                hash.add(val)
