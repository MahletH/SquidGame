class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        min_ = k
        for i in range(k):
            if blocks[i] == "W":
                countW += 1
        min_ = min(min_, countW)
        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                countW += 1
            if blocks[i-k] == "W":
                countW -= 1
            min_ = min(min_, countW)
        return min_
