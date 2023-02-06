class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            cnt += 1 if word.startswith(pref) else 0 
        return cnt