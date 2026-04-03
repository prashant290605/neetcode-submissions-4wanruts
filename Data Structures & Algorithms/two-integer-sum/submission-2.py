class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        hash = {}
        for i in range(n):
            if nums[i] in hash.keys():
                ans.append(hash[nums[i]])
                ans.append(i)
                return ans
            else:
                hash[target-nums[i]] = i
            
        return ans