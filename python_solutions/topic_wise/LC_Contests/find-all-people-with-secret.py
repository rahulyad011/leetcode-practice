class Solution:
def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    
    meetings.sort(key=lambda x:x[2])
    groups = itertools.groupby(meetings,key = lambda x:x[2])
    
    sh = {0,firstPerson}
    for key,grp in groups:
        seen = set()
        graph = defaultdict(list)
        for a,b,t in grp:
            graph[a].append(b)
            graph[b].append(a)
            if a in sh:
                seen.add(a)
            if b in sh:
                seen.add(b)
        
        queue = deque(seen)
        while queue:
            node = queue.popleft()
            for neig in graph[node]:
                if neig not in sh:
                    sh.add(neig)
                    queue.append(neig)
        
    return list(sh)