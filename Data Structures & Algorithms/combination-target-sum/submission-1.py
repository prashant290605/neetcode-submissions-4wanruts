class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(idx,path,sm):
            if sm == target:
                res.append(path[:])
                return 
            
            for j in range(idx,len(nums)):
                if nums[j] + sm > target:
                    return
                path.append(nums[j])
                backtracking(j,path,sm+nums[j])
                path.pop()
                
        backtracking(0,[],0)
        return res