class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = set(nums1)
        v = set(nums2)
        k = k.intersection(v)
        return list(k)