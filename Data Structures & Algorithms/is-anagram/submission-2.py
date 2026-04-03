class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = [0]*26
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        for i in range(n1):
            hash[ord(s[i])-ord('a')] += 1
            hash[ord(t[i]) - ord('a')] -= 1
        for i in hash:
            if i != 0:
                return False
        return True