class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = float('-inf')
        curr = 0

        for i in nums:
            curr = curr+i
            ma = max(ma,curr)

            if curr<0:
                curr=0

        return ma