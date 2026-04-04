class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ct = Counter(s)
        output = []
        l = 0
        st = set()
        for r in range(len(s)):
            ch = s[r]
            st.add(ch)
            ct[ch] -= 1
            if ct[ch] == 0:
                st.remove(ch)
            if not st:
                output.append(r-l+1)
                l = r+1
        return output