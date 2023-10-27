"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        def bfs(root):
            queue = deque()
            graph = {}
            # create new node
            if not root:
                return None
            clone = Node(root.val, None)
            queue.append((root, clone))
            visited.add(root)
            graph[root.val] = clone
            while(queue):
                curr, currclone = queue.popleft()
                for neigh in curr.neighbors:
                    nclone = None
                    if neigh.val in graph:
                        nclone = graph[neigh.val]
                    else:
                        nclone = Node(neigh.val, None)
                        graph[neigh.val] = nclone
                    currclone.neighbors.append(nclone)
                    if neigh not in visited:
                        queue.append((neigh, nclone))
                        visited.add(neigh)
            return clone
        newgraph = bfs(node)
        return newgraph

            

        