class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=defaultdict(int)

        for i in nums:
            count[i]+=1
        
        k = list(dict(count).items())
        k.sort(key=lambda x:x[1],reverse=True)
        count=k[0][1]
        for i in range(1,len(k)):
            if k[i][1]==k[0][1]:
                count = count+k[i][1]
            else:
                return count
        return count