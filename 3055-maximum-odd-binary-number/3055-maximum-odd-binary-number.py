class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        s.sort(reverse=True)
        return "".join(s[1:]+['1'])
