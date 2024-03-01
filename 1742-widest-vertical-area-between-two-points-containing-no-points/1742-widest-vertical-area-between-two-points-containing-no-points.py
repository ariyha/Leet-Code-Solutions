class Solution:
    def maxWidthOfVerticalArea(self, l: List[List[int]]) -> int:
        l.sort(key=lambda x:x[0])
        max = l[0][0]-l[1][0]
        for i in range(1,len(l)):
            if l[i][0]-l[i-1][0]>max:
                max=l[i][0]-l[i-1][0]
        return max