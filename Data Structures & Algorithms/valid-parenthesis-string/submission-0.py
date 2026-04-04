class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0  # maximizing (
        low = 0   # minimizing (
        for i in s:
            if i == '(':
                high += 1
                low += 1
            elif i == ')':
                high -= 1
                low -= 1
            else:
                high += 1
                low -= 1
            
            if high < 0:
                return False
            low = max(0,low)
        return low == 0