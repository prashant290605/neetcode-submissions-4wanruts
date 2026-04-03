from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0]*numCourses #0-unvisited, 1-visiting, 2-visited

        hash = defaultdict(list)
        for a,b in prerequisites:
            hash[a].append(b)
        ans = []
        def dfs(node):

            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            for i in hash[node]:
                if not dfs(i):
                    return False
            visited[node] = 2
            ans.append(node)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []

        return ans
        