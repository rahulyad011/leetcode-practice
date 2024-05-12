# https://leetcode.com/problems/course-schedule/

"""
Solution:
# this is standard problem of top logical sorting
# as the nodes are to be visited in a specific order, i.e. prerequisites first and then the dependents
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeMap = {}
        queue = collections.deque()
        order = []
        
        #check in degree and make the graph
        # intialize the graph:
        for node_id in range(numCourses):
            nodeMap[node_id] = {
                "in" : 0,
                "out" : []}
        for edge in prerequisites:
            nodeMap[edge[1]]["in"] += 1
            nodeMap[edge[0]]["out"].append(edge[1])
        
        for item in nodeMap.keys():
            # this means this node does not have any prerequites
            if nodeMap[item]["in"] == 0:
                queue.append(item)
    
        while queue:
            # this means this node does not have any prerequites
            currnode = queue.popleft()
            # updating the in count of all the out links of this node
            for link in nodeMap[currnode]["out"]:
                nodeMap[link]["in"]-=1
                if nodeMap[link]["in"] == 0:
                    queue.append(link)
            order.append(currnode)
            del nodeMap[currnode]

        if len(order) == numCourses:       
            return True
        else:
            return False
        