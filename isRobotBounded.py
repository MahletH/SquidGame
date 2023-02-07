class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        for inst in (instructions * 4):
            if inst == 'G':
                pos[0] += dirs[i][0]
                pos[1] += dirs[i][1]
            elif inst == 'L':
                i = (i - 1) % 4
            else:
                i = (i + 1) % 4
        return pos == [0,0]