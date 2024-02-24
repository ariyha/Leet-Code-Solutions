class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = set((0,firstPerson))

        meet_sort=[]
        meetings.sort(key=lambda x:x[2])

        seen = set()

        for meeting in meetings:
            if meeting[2] not in seen:
                seen.add(meeting[2])
                meet_sort.append([])
            meet_sort[-1].append((meeting[0],meeting[1]))
        
        for group in meet_sort:
            known_people = set()
            graph = defaultdict(list)

            for p1,p2 in group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known:
                    known_people.add(p1)
                if p2 in known:
                    known_people.add(p1)
            
            queue =deque((known_people))

            while(queue):
                curr=queue.popleft()
                known.add(curr)
                for i in graph[curr]:
                    if i not in known:
                        known.add(i)
                        queue.append(i)
                    
        return list(known)
