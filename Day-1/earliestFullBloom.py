class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = [(growTime[i],plantTime[i]) for i in range(len(plantTime))]
        plants.sort(reverse=True)
        tot, cur = 0, 0
        for grow,plant in plants:
            cur += plant
            tot = max(tot, cur + grow)
        return tot
