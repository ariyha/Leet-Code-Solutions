class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = set()

        mx=max(nums,default=0)

        for i in nums:
            mp.add(i)
        
        for i in range(1,mx):
            if i not in mp:
                return i
        
        if mx<0:
            return 1
        else:
            return mx+1
