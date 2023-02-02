class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros, ones = [0], [0]
        for c in s:
            zeros.append(zeros[-1]+int(c=='0'))
            ones.append(ones[-1]+int(c=='1'))
        tot = zero = one = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == '1':
                tot += zeros[i] * zero
                one += 1
            else:
                tot += ones[i] * one
                zero += 1
        return tot