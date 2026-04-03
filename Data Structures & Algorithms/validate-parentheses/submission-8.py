class Solution:
    def isValid(self, s: str) -> bool:
        a = deque()
        x = {')':'(',']':'[','}':'{'}
        n = len(s)
        for i in range(n):
            if s[i] not in x:
                a.append(s[i])
            else:
                if len(a) == 0:
                    return False
                c = a.pop()
                if c != x[s[i]]:
                    return False
                
        return len(a) == 0