class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thresh: int) -> int:

        g = [[float('inf')]*n for i in range(n)]
        for i in range(n):
            g[i][i]=0

        for n1,n2,d in edges:
            g[n1][n2]=d
            g[n2][n1]=d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if g[i][k]<float('inf') and g[k][j]<float('inf'):
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        out = -1
        city_cnt = float('inf')
        for i in range(n-1,-1,-1):
            count = 0

            for j in range(n):
                if g[i][j]<=thresh and i!=j:
                    count+=1
            
            if count<city_cnt:
                out=i
                city_cnt=count
        
        return out