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
            path.append(nums[idx])
            dfs(idx+1,path,sm+nums[idx])
            path.pop()
            dfs(idx+1,path,sm)
        dfs(0,[],0)
        ans = []
        for i in res:
            if i not in ans:
                ans.append(i)
        return ans