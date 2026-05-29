class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for i in strs:
            ans += i
            ans += '.'
    
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        x = ''
        for i in range(len(s)):
            if s[i] == '.':
                ans.append(x)
                x = ''
            else:
                x += s[i]
        return ans