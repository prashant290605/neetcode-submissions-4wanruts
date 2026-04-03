class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)
        hash = {}
        for i in range(n):
            hash[target-nums[i]] = i
        for i in range(n):
            if nums[i] in hash and hash[nums[i]] != i:
                ans.append(i)
                ans.append(hash[nums[i]])
                return ans