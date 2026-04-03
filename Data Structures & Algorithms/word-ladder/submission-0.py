class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0

        wordset = set(wordList)
        dis = 0
        q = deque([beginWord])
        while q:
            dis += 1
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return dis
                for j in range(len(node)):
                    for k in range(97,123):
                        if chr(k) == node[j]:
                            continue
                        x = node[:j] + chr(k) + node[j+1:]
                        if x in wordset:
                            q.append(x)
                            wordset.remove(x)
        return 0
