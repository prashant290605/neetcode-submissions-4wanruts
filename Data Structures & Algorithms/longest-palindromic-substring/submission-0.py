class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''

        st = ''
        n = len(s)
        for i in range(n):
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            a = s[l+1:r]
            if len(a) >= len(st):
                st = a
            
            l = i-1
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            a = s[l+1:r]
            if len(a) >= len(st):
                st = a
        return st