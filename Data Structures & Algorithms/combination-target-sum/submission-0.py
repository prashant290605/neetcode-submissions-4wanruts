class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(idx,path,sm):
            if sm >= target:
                if sm == target:
                    res.append(path[:])
                return
            if idx == len(nums):
                return
            path.append(nums[idx])
            sm += nums[idx]
            backtracking(idx,path,sm)
            sm -= nums[idx]
            path.pop()
            if idx+1 < len(nums):
                backtracking(idx+1,path,sm) 
        backtracking(0,[],0)
        return res