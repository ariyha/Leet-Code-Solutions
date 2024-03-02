class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxi=0

        while(j<len(prices)):
            profit = prices[j]-prices[i]
            if profit>0:
                maxi=max(maxi,profit)
            else:
                i=j
            j=j+1
        
        return maxi