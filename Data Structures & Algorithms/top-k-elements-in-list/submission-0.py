class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hash = {}
        freq = [[] for _ in range(n+1)]
        for i in nums:
            hash[i] = 1 + hash.get(i,0)
        for num,cnt in hash.items():
            freq[cnt].append(num)
        
        ans = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans