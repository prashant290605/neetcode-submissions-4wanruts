class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = {}
        for i , n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff],i]
            hash[n] = i