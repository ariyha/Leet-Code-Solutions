class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum1=0
        lenmax=0
        mp={}

        for i in range(len(nums)):
            num = nums[i]
            sum1+=1 if num==1 else -1
            if sum1==0:
                lenmax=i+1
            elif sum1 in mp:
                lenmax = max(lenmax,i-mp[sum1])
            else:
                mp[sum1]=i
        
        return lenmax