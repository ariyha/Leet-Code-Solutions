class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = nums[0]
        curr = nums[0]

        for i in nums[1:]:
            curr = curr+i
            ma = max(ma,curr)

            if curr<0:
                curr=0

        return ma