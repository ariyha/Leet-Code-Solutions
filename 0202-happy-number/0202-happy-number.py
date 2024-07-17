class Solution:
    def isHappy(self, n: int) -> bool:
        known = []
        while(n not in known and n!=1):
            known.append(n)
            n = str(n)
            n = sum([int(i)**2 for i in n])
            
        print(known)
        if n==1:
            return True
        
        return False