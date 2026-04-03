"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i.start)
        start,end = intervals[0].start,intervals[0].end

        for i in range(1,len(intervals)):
            a,b = intervals[i].start,intervals[i].end
            if a < end:
                return False
            else:
                start = a
                end = b
        return True