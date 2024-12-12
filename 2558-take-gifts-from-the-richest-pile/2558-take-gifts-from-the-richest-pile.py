import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            m = getmax(gifts)
            gifts[m] = math.floor(math.sqrt(gifts[m])) 
        return sum(gifts)
def getmax(arr):
    i=1
    maxi=arr[0]
    curr=0

    while(i<len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
            curr=i
        
        i+=1
    
    return curr