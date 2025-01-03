class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l=count=0
        r=sum(nums)
        for i in range(len(nums)-1):
            l += nums[i]
            r -= nums[i]
            if l>=r:
                count+=1
        return count
