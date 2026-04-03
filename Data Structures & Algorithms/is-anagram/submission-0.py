class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        
        hash = {}
        for i in range(n1):
            if s[i] in hash:
                hash[s[i]] += 1
            else:
                hash[s[i]] = 1
            if t[i] in hash:
                hash[t[i]] -= 1
            else:
                hash[t[i]] = -1
        
        for i in range(n1):
            if hash[s[i]] != 0:
                return False
        return True