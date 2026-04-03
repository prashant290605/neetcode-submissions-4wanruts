class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        intervals = deque(intervals)
        ans = 0
        [start,end] = intervals.popleft()
        while intervals:
            [a,b] = intervals.popleft()
            if a < end:
                ans += 1
                if end > b:
                    end = b
                    start = a
            else:
                start = a
                end = b
        return ans
