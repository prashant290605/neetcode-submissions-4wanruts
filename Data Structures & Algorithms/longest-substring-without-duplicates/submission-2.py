class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[l])
                l += 1
            char.add(s[i])
            ans = max(ans,i-l+1)
        return ans