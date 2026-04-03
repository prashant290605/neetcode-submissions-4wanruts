class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = []
    
        for i in range(k):
            x.append(nums[i])
        heapq.heapify(x)
        for i in range(k,len(nums)):
            if nums[i] > x[0]:
                a = heapq.heappop(x)
                heapq.heappush(x,nums[i])
        return x[0]