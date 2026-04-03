class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l = i+1
            r = n-1
            while l < r:
                s = nums[l] + nums[r]

                if s == target:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

                     
                elif s < target:
                    l += 1
             
                elif s > target:
                    r -= 1
         
        return ans
