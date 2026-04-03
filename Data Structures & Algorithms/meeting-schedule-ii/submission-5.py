class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda i: i.start)

        rooms = {}
        rooms[1] = [intervals[0].start, intervals[0].end]
        ans = 1

        for i in range(1, len(intervals)):
            a, b = intervals[i].start, intervals[i].end
            done = False

            for j in rooms:
                x, y = rooms[j]

               
                if a >= y:
                    rooms[j] = [a, b]
                    done = True
                    break

            if not done:
                ans += 1
                rooms[ans] = [a, b]

        return ans