class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        min_heap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                r,l = intervals[i][1],intervals[i][0]
                heapq.heappush(min_heap,(r-l+1,r))
                i += 1
            
            while min_heap and q > min_heap[0][1]:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        
        return [res[q] for q in queries]