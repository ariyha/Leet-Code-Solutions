class Solution:
    def rotate(self, nums: List[int], k: int):
        n = len(nums)
        k=k%n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])