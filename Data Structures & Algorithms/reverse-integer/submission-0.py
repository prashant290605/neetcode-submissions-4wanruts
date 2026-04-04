class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        def rev(n,rec):
            if n == 0:
                return rec
            
            rec = (rec*10 + n%10)
            return rev(n//10,rec)
        
        if x < 0:
            sign = -1
        x = abs(x)
        
        ans = rev(x,0)
        ans *= sign
        if ans < -(1<<31) or ans > (1<<31) - 1:
            return 0
        return ans