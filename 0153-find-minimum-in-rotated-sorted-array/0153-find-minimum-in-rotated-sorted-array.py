class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            if nums[low] <= nums[high]:
                return nums[low]
            mid = low + int((high - low) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
