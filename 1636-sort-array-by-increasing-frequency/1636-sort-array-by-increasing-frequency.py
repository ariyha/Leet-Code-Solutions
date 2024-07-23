class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums),key = lambda x:nums.count(x),reverse=True )[::-1]
