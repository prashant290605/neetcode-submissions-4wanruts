class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = []
        while l <= r:
            a = numbers[l] + numbers[r] 
            if a == target:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif a > target:
                r -= 1
                continue
            else:
                l += 1
                continue
        return ans