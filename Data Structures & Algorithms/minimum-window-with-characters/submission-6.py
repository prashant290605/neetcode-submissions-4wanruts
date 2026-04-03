class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        count_t = {}
        window = {}
        have = 0
        ans = [-1,-1]
        len_ans = float('inf')
        l = 0

        for i in t:
            count_t[i] = 1 + count_t.get(i,0)
        need = len(count_t)
        for i in range(len(s)):
            c = s[i]
            window[c] = 1 + window.get(c,0)
                
            if c in count_t and window[c] == count_t[c]:
                    have += 1
            while have == need:
                if i-l+1 < len_ans:
                    ans = [l,i]
                    len_ans = i-l+1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
        [a,b] = ans

        return s[a:b+1] if len_ans != float('inf') else ''
