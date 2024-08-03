from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = Counter(target)
        b = Counter(arr)
        return a==b