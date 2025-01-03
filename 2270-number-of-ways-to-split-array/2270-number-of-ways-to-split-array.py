class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l=0
        count=0
        r=sum(nums)
        for i in range(len(nums)-1):
            l = l+nums[i]
            r = r - nums[i]
            if l>=r:
                count+=1
        
        return count
