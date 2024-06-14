class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        vis=[]
        nums.sort()
        i=1
        count=0
        while(i<len(nums)+1):
            if nums[i] <=nums[i-1]:
                count+=nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
            i+=1
        
        return count

