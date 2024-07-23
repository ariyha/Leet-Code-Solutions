class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = sorted(nums,key = lambda x:nums.count(x),reverse=True )
        return out[::-1]