# https://leetcode.com/problems/time-taken-to-cross-the-door

""" Solution:
This is fairly straight forward solution but a bit of lenghty.
So the idea is similar to the traffic control problem, we maitain two queue and maintain the traffic at the door according to the rules
You can insert the element in the queue in the final loop itself but I wrote a cleaner version of code using two loops
Time : O(n) + O(max(t, n))
Space : O(n) for the two queues
"""

from collections import deque

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        queue_in = deque()
        queue_out = deque()
        max_time = max(arrival)
        # lets prepare the in and out queues
        for i in range(len(arrival)):
            if state[i]:
                queue_out.append((arrival[i], i))
            else:
                queue_in.append((arrival[i], i))

        result = [-1]*len(arrival)
        previous_state = -1
        # print(queue_in, queue_out)
        t = 0
        while queue_in or queue_out:
            enter_person = None
            exit_person = None
            if len(queue_in) and queue_in[0][0] <= t:
                enter_person = queue_in[0]
            if len(queue_out) and queue_out[0][0] <= t:
                exit_person = queue_out[0]
            # making a the choice to allow enter of exist
            choice = None
            if enter_person and exit_person:
                if len(queue_out) and (previous_state == -1 or previous_state ==1):
                    choice = queue_out.popleft()
                    result[choice[1]] = t
                else:
                    if len(queue_in):
                        choice = queue_in.popleft()
                        result[choice[1]] = t
            elif len(queue_in) and enter_person and not exit_person :
                choice = queue_in.popleft()
                result[choice[1]] = t
            elif len(queue_out) and not enter_person and exit_person:
                choice = queue_out.popleft()
                result[choice[1]] = t
            if choice:
                previous_state = state[choice[1]]
            else:
                previous_state = -1
            t+=1
        return result