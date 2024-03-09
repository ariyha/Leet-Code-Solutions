class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a = set(nums1)
        b = set(nums2)

        x = list(a.intersection(b))
        if len(x)==0:
            return -1
        x.sort()


        return x[0]