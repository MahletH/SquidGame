class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [(ages[i],scores[i]) for i in range(len(scores))]
        players.sort(reverse=True)
        dp = [players[i][1] for i in range(len(scores))]
        for i in range(len(scores)):
            for j in range(i):
                if players[j][1]>= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
