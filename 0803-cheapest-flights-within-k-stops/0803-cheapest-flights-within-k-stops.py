class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        paths={}
        for i in flights:
            if i[0] not in paths:
                paths[i[0]]=[(i[1],i[2])]
            else:
                paths[i[0]].append((i[1],i[2]))
            
        dist = [float('inf')]*n
        dist[src]=0

        q=[(src,0)]
        k1=0

        while(q!=[] and k1<=k):
            l = len(q)
            for i in range(l):
                node,x = q.pop(0)

                if node not in paths: continue

                for neigh,y in paths[node]:
                    if x+y>=dist[neigh]:
                        continue
                    
                    dist[neigh]=x+y
                    q.append((neigh,dist[neigh]))
            k1+=1

        if dist[dst]==float('inf'):
            return -1
        else:
            return dist[dst]