
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        ans = []
        n = len(nums)
        for i in range(n):
            hash[nums[i]] = 1 + hash.get(nums[i],0)
        freq = [[] for _ in range(n+1)]
        for num , cnt in hash.items():
            freq[cnt].append(num)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
