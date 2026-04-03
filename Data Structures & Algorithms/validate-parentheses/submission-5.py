class Solution:
    def isValid(self, s: str) -> bool:
        a = deque()
        bracket = {'(':')','{':'}','[':']'}
        for i in s:
            if i in bracket:
                a.append(bracket[i])
            else:
                if len(a) == 0:
                    return False
                c = a.pop()
                if c != i:
                    return False
        return len(a) == 0