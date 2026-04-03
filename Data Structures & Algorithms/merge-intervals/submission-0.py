class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals = deque(intervals)
        ans = []
        [start,end] = intervals.popleft()
        while intervals:
            [a,b] = intervals.popleft()
            if a <= end:
                end = max(end,b)
            else:
                ans.append([start,end])
                start = a
                end = b
        ans.append([start,end])
        return ans