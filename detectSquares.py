class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x = defaultdict(set)
    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])] += 1
        self.x[point[0]].add(point[1])
    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0
        for i in self.x[x]:
            if i != y: 
                res += (self.points[(x, i)] 
                * self.points[(x + i - y, y)] 
                * self.points[(x + i - y, i)]
                + self.points[(x, i)] 
                * self.points[(x + y - i, y)] 
                * self.points[(x + y - i, i)])
        return res
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)