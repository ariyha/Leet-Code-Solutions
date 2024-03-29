class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n=len(nums)
        count=0
        r=l=0

        while(r<n):
            if nums[r]==mx:
                k-=1
            r+=1

            while(k==0):
                if nums[l]==mx:
                    k+=1
                l+=1
            count+=l
        
        return count