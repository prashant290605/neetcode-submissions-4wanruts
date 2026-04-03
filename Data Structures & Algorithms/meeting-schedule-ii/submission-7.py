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

        hash = {}
        start,end = intervals[0].start,intervals[0].end
        hash[1] = [start,end]
        ans = 1
        x = len(hash)

        for i in range(1,len(intervals)):
            a,b = intervals[i].start,intervals[i].end
            done = False
            for j in hash:
                x,y = hash[j][0],hash[j][1]
                if y <= a:
                    hash[j] = [a,b]
                    done = True
                else:
                    continue
                if done:
                    break
            if not done:
                ans += 1
                hash[ans] = [a,b]
        return ans
            
