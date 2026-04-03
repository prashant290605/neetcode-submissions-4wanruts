class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in range(len(strs)):
            sorteds = ''.join(sorted(strs[i]))
            ans[sorteds].append(strs[i])
        
        return list(ans.values())