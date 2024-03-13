class Solution:
    def pivotInteger(self, n: int) -> int:
        nsum = (n*(n+1))/2
        currsum=0

        for i in range(1,n+1):
            currsum=currsum+i
            if currsum==nsum:
                return i
            nsum=nsum-i
        
        return -1