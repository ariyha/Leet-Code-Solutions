class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]

        out=[]
        for i in nums:
            k=nums.copy()
            k.remove(i)
            l = self.permute(k)
            for j in l:
                out.append([i]+j)
        return out
