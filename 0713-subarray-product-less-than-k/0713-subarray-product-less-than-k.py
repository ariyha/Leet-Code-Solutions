class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        
        n=len(nums)
        prod=1
        count=0
        l=r=0
        while(r<n):
            prod = prod*nums[r]
            r+=1
            while(l<r and prod>=k):
                prod=prod/nums[l]
                l+=1
            count=count+(r-l)
        
        return count
