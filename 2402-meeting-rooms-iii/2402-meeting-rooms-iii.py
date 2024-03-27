class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy=[]
        available=[i for i in range(n)]
        count=[0]*n
        meetings.sort()
        for start,end in meetings:
            while busy and busy[0][0]<=start:
                _end,room=heapq.heappop(busy)
                heapq.heappush(available,room)

            if available:
                room=heapq.heappop(available)
                heapq.heappush(busy,(end,room))
            else:
                time,room=heapq.heappop(busy)
                heapq.heappush(busy,(time+end-start,room))
            count[room]+=1
        return count.index(max(count))      
