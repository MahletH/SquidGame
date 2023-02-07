class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            ans += -1 if log == "../" and ans else int(log != "./" and log != "../")
        return ans