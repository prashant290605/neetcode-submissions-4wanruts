"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        interval = []
        for i in range(len(intervals)):
            interval.append([intervals[i].start,intervals[i].end])
        interval.sort()

        print(interval)
        x,y = interval[0][0],interval[0][1]
        for i in range(1,len(interval)):
            if interval[i][0] < y:
                return False
            else:
                x,y = interval[i][0],interval[i][1]
        
        return True