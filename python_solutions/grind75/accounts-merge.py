# https://leetcode.com/problems/accounts-merge/

from collections import deque, defaultdict

"""
solution:
accountsMerge this is a good graph proble, it is standrd problem for uniion find but can also be done with DFS or BFS. I tried with BFS, not a optimal solution but it works if we design the graph well. I mean the idea is to find emails that are connected and map it to just one graph
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
                    
        visited = set()
        # graph to map the final accounts and emails
        graph = defaultdict(set)
        # build the graph
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
        # print(graph)

        # bfs to check all connected emails and map them to one account in a sorted order
        queue = deque()
        def bfs(startnode):
            queue.append(startnode)
            commonemails = set()
            while queue:
                currnode = queue.popleft()
                visited.add(currnode)
                commonemails.add(currnode)
                for neigh in graph[currnode]:
                    if neigh not in visited:
                        queue.append(neigh)
            commonemails = list(commonemails)
            commonemails.sort()
            return commonemails

        result = []
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in visited:
                    connected_emails = bfs(email)
                    temp = [name]
                    for connection in connected_emails:
                        temp.append(connection)
                    result.append(temp)
        return result
        