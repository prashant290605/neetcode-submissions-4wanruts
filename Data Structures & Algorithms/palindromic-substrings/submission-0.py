class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.count_pal(s,i,i)
            ans += self.count_pal(s,i,i+1)
        return ans
    
    def count_pal(self,s,l,r):
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans