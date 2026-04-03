class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        if len(intervals) == 0:
            return []
        
        intervals.sort()
        intervals = deque(intervals)
        ans = []
        [start , end] = intervals.popleft()

        while len(intervals) != 0:
            [a , b] = intervals.popleft()
            if a <= end:
                end = max(end,b)
            else:
                ans.append([start , end])
                start = a
                end = b
        ans.append([start,end])
        return ans