class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins =[]
        for i in range(len(matrix)):
            mins.append(min(matrix[i]))
        
        maxs = []
        for i in range(len(matrix[0])):
            maxi = -10000000
            for j in range(len(matrix)):
                maxi = max(matrix[j][i],maxi)
            maxs.append(maxi)

        out =[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    if matrix[i][j]==mins[i] and matrix[i][j]==maxs[j]:
                        out.append(matrix[i][j])

        return out