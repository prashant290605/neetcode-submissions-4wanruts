class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.n = 0
    def addNum(self, num: int) -> None:
        self.n += 1
        if len(self.minheap) == len(self.maxheap):
            if len(self.minheap) == 0:
                heapq.heappush(self.minheap,num)
            else:
                if num > self.minheap[0]:
                    heapq.heappush(self.minheap,num)
                else:
                    heapq.heappush(self.maxheap,num*-1)
        else:
            if len(self.minheap) > len(self.maxheap):
                if num > self.minheap[0]:
                    x = heapq.heappop(self.minheap)
                    heapq.heappush(self.maxheap,x*-1)
                    heapq.heappush(self.minheap,num)
                else:
                    heapq.heappush(self.maxheap,num*-1)
            else:
                if num < self.maxheap[0] * -1:
                    x = heapq.heappop(self.maxheap)
                    heapq.heappush(self.minheap,x*-1)
                    heapq.heappush(self.maxheap,num*-1)
                else:
                    heapq.heappush(self.minheap,num)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0]+self.maxheap[0]*-1)/2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return self.maxheap[0]*-1