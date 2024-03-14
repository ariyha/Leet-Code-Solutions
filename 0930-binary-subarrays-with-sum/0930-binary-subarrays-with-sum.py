class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr = 0
        count = 0
        d1 = {0:1}

        for i in nums:
            curr = curr+i
            if curr-goal in d1:
                count+=d1[curr-goal]
            
            d1[curr]=d1.get(curr,0)+1
        
        return count