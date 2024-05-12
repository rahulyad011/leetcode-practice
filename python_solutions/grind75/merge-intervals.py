# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        result = []
        if not intervals:
            return result
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                start = min(intervals[i][0], result[-1][0])
                end = max(intervals[i][1], result[-1][1])
                result[-1] = [start, end]
        return result