class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        space = set(nums)
        ans = 0
        for i in range(n):
            if nums[i]-1 not in space:
                length = 0
                while nums[i] + length in space:
                    length += 1
                ans = max(ans, length)
        return ans