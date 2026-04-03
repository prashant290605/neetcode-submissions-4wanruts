class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hash = {}
        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        
        for i in hash:
            if hash[i] > 1:
                return True
        return False