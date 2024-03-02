class Solution:
    def sortedSquares(self, l: List[int]) -> List[int]:
        i=0
        while(l[i]<0):
            i=i+1
        
        key2=i
        j=i
        i=j-1

        k=[]

        while(i>=0 and j<len(l)):
            if l[i]**2>l[j]**2:
                k.append(l[j]**2)
                j+=1
            else:
                k.append(l[i]**2)
                i-=1
        
        if i==-1:
            while(j<len(l)):
                k.append(l[j]**2)
                j+=1
        elif j==key2:
            while(i>=0):
                k.append(l[i]**2)
                i+=1
        
        return k       
