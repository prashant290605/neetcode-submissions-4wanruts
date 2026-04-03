class Solution:
    def isValid(self, s: str) -> bool:
        a = deque()
        b = {'(':')' , '{':'}' , '[':']'}
        for i in s:
            if i == '(' or i == '{' or i == '[':
                a.append(i)
            else:
                if len(a) == 0:
                    return False
                c = a.pop()
                if b[c] != i:
                    return False
        return len(a) == 0