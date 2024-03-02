class Solution:
    def sortedSquares(self, l: List[int]) -> List[int]:
        l.sort(key=lambda x:abs(x))
        l = [i**2 for i in l]
        return l