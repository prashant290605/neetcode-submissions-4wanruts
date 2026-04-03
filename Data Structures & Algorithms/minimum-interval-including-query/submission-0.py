class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n = len(queries)
        ans = [0 for _ in range(n)]
        for i in range(n):
            m = float('inf')
            for [a,b] in intervals:
                if b < queries[i]:
                    pass
                if a <= queries[i] <= b:
                    m = min(m,b-a+1)
            if m == float('inf'):
                m = -1
            ans[i] = m
        return ans
            