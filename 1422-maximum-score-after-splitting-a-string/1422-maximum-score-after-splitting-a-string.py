class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1,len(s)):
            score = max(score,list(s[0:i]).count('0')+list(s[i:]).count('1'))
        return score