# https://leetcode.com/contest/weekly-contest-370/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        rev = set()
        for node in edges:
            r = node[1]
            rev.add(r)
        count = 0
        winner = -1
        for i in range(n):
            if i not in rev:
                count+=1
                winner = i
        if count==1:
            return winner
        else:
            return -1
            