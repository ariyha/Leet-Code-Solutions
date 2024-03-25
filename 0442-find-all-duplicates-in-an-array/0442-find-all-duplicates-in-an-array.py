class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited=set()
        out=set()
        for num in nums:
            if num in visited:
                out.add(num)
            visited.add(num)
        return out
            
