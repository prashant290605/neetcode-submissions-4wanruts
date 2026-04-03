class PrefixTree:

    def __init__(self):
        self.hashset = set()

    def insert(self, word: str) -> None:
        self.hashset.add(word)

    def search(self, word: str) -> bool:
        if word in self.hashset:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        y = list(self.hashset)
        for i in y:
            if len(i) < n:
                continue
            if i[:n] == prefix:
                return True
    
        return False
        