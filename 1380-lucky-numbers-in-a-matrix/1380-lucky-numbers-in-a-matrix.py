class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins =[]
        for i in range(len(matrix)):
            mins.append(min(matrix[i]))
        
        columns = list(zip(*matrix))
        maxs = []
        for i in range(len(columns)):
            maxs.append(max(columns[i]))

        out =[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                v=matrix[i][j]
                    if v==mins[i] and v==maxs[j]:
                        out.append(matrix[i][j])
        return out