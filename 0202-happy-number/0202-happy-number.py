class Solution:
    def isHappy(self, n: int) -> bool:
        known = set()
        if n==1 or n==7:
            return True

        while(n not in known and n!=1 and n!=7):
            known.add(n)
            n = str(n)
            n = sum([int(i)**2 for i in n])
            
        if n==1 or n==7:
            return True
        
        return False