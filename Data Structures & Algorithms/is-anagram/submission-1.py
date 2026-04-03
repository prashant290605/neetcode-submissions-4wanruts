class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = defaultdict(int)
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        for i in range(n1):
            hash[s[i]] += 1
            hash[t[i]] -= 1
        for i in hash.values():
            if i != 0:
                return False
        return True