class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)
        l = 0
        r = 0
        ans = 0
        while r < n :
            x = 0
            count[s[r]] = 1 + count.get(s[r],0)
            if r - l - max(count.values()) <= k - 1:
                x = (r-l+1)
            else:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans,x)
            r += 1
        return ans