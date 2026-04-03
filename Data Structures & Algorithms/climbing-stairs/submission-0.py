class Solution:
    store = {}
    def climbStairs(self, n: int) -> int:
        
        if n <= 0:
            return 1
        elif n == 1:
            return 1
        else:
            if n in self.store:
                return self.store[n]
            else:
                if n >= 2:
                    self.store[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                else:
                    self.store[n] = self.climbStairs(n-1)
                return self.store[n]