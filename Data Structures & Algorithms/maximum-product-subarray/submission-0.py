class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        cur_max = 1
        cur_min = 1

        for x in nums:
            temp = cur_max * x
            cur_max = max(cur_max * x, cur_min * x , x)
            cur_min = min(temp , cur_min * x , x)
            ans = max(ans,cur_max)
        return ans