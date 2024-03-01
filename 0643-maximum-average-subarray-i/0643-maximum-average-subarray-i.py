class Solution:
    def findMaxAverage(self, nums: List[int], n: int) -> float:
         ma=sum(nums[0:n])
         k=ma


         for i in range(n,len(nums)):
             k +=nums[i]
             k -=nums[i-n]
             if k>ma:
                 ma=k
        
         return ma/n