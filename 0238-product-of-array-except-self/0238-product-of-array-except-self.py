class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        prod =1
        other=0

        for i in nums:
            if i==0:
                other+=1
                continue
            prod = prod*i
        
        for i in nums:
            if i==0:
                if other>1:
                    out.append(0)
                else:
                    out.append(prod)
            else:
                if other>0:
                    out.append(0)
                    continue
                out.append(prod//i)
        
        return out