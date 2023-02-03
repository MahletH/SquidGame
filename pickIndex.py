class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        tot = 0
        for i in w:
            tot += i
            self.prefix.append(tot)
        self.tot = tot

    def pickIndex(self) -> int:
        random_index = random.randint(1, self.tot)
        return bisect.bisect_left(self.prefix, random_index) 