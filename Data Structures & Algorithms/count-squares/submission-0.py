class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptcnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptcnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.pts:
            if (abs(px-x) != abs(py-y)) or x == px or y == py:
                continue
            res += self.ptcnt[(px,y)] * self.ptcnt[(x,py)]
        return res
