from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            ans[key].append(i)
        return list(ans.values())
