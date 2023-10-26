class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=0
        r=0
        result = []
        ind = 0
        done = 0
        if not intervals:
            return [newInterval]
        while ind < len(intervals):
            # after case: new interval start > curr interval end -- non-overlapping
            if intervals[ind][1] < newInterval[0] or done:
                result.append(intervals[ind])
                ind+=1
            # before case: new interval ends before the curr interval -- nonoverlapping
            elif intervals[ind][0] > newInterval[1]:
                result.append(newInterval)
                done =1
            # durring case: this is important case new interval is overlapping with other intervals
            # we capture the overlapping part with min and max and then create updated newinterval 
            # this newinterval contains part of curr interval also, this way we iterate and compare 
            # with next interval
            else:
                start = min(intervals[ind][0], newInterval[0])
                end = max(intervals[ind][1], newInterval[1])
                newInterval= (start, end)
                ind+=1
        if not done:
            result.append(newInterval)
        return result