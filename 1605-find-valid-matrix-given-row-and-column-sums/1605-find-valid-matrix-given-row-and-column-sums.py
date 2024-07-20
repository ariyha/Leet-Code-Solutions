# class Solution:
#     def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

#         n = len(rowSum)
#         m = len(colSum)
#         i,j = 0,0

#         arr = []
#         for i in range(m):
#             arr.append([0]*n)

#         while(i<n and j<m):
#             x = min(rowSum[i],colSum[j])
#             arr[i][j]=x

#             rowSum[i]-=x
#             colSum[j]-=x

#             if rowSum[i]==0:
#                 i+=1
            
#             if colSum[j]==0:
#                 j+=1

#         return arr

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        numRows = len(rowSum)
        numCols = len(colSum)
        result = [[0] * numCols for _ in range(numRows)]

        i, j = 0, 0

        while i < numRows and j < numCols:
            val = min(rowSum[i], colSum[j])
            result[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return result
