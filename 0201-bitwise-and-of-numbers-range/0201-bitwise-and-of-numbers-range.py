class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        n=0
        while(left!=right):
            left=left>>1
            right=right>>1
            n+=1
        
        return left<<n