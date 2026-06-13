"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda i:i.start)
        heap = []
        heapq.heappush(heap,intervals[0].end)
        ans = 1
        for i in range(1,len(intervals)):
            x = intervals[i].start
            if x < heap[0]:
                ans += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)

        return ans