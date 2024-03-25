class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        out=[]
        prev=nums[0]

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and nums[i] not in out:
                out.append(nums[i])
        
        return out