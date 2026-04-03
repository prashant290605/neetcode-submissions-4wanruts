class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float('inf')
        
        while l <= r:
            mid = (l+r)//2
            hrs = 0
            for i in piles:
                hrs += (i+mid-1)//mid
            if hrs > h:
                l = mid + 1
            else:
                ans = min(mid,ans)
                r = mid - 1
        return ans 