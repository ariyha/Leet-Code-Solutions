class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s).sort(reverse=True)
        k = "".join(s[1:])
        k=k+'1'
        return k