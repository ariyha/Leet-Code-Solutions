class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = -100000
        curr = 0
        for i in nums:
            curr +=i
            if curr>ma:
                ma=curr
            ma = max(ma,curr)
            if curr<0:
                curr=0
        return ma