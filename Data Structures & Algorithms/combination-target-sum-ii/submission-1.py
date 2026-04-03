class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(idx,path,sm):
            if sm == target:
                res.append(path[:])
                return
            if idx == len(nums) or sm > target:
                return
            
            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                if sm + nums[i] > target:
                    return 
                path.append(nums[i])
                dfs(i+1,path,sm+nums[i])
                path.pop()
        dfs(0,[],0)
        return res