# https://leetcode.com/problems/reward-top-k-students/

from heapq import heapify, heappush, heappop

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # positive_feedback
        # negative_feedback
        # student_id[i] --> report[i]
        # top k students
        # s1-points, index, s2 - points, index, s3 - points, index
        # calculate_points --> (report, student) +3 pos and -1 for neg

        """solution: 
        first make the pos and neg feedback as set for efficient check
        there are two solutions:
        1. use dictnary and save the student_id : points, then sort it with (lambda x : x[1], -x[0])
        2. use a max heap and save the (-points, student_id), then take the top k from the heap
        3. space optimized heap -- take a min heap and save only the top k max values (points, -student_id)
            This can be done by checking the heap top < curr
        """

        """dict solution"""
        positive_feedback_set = set(positive_feedback)
        negative_feedback_set = set(negative_feedback)

        def calculate_points(words):
            score = 0
            for word in words.split():
                if word in positive_feedback_set:
                    score+=3
                if word in negative_feedback_set:
                    score-=1
            return score
        dict_students = {}

        for i, student_report in enumerate(report):
            student_point = calculate_points(student_report)
            dict_students[student_id[i]] = student_point

        sorted_students = sorted(dict_students.items(), key = lambda x : (x[1], -1*x[0]), reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_students[i][0])
        return result


        """min heap solution (debug fails in some test cases)"""
        # def calculate_points(words):
        #     score = 0
        #     for word in words.split():
        #         if word in positive_feedback:
        #             score+=3
        #         if word in negative_feedback:
        #             score-=1
        #     print(score)
        #     return score

        # # min_heap
        # heap = []
        # heapify(heap)

        # for i, student_report in enumerate(report):
        #     student_point = calculate_points(student_report)
        #     if len(heap) < k:
        #         heappush(heap, (student_point, -1*student_id[i]))
        #     else:
        #         if (student_point, -1*student_id[i]) > heap[0]:
        #             heappop(heap)
        #             heappush(heap, (student_point, -1*student_id[i]))
        
        # # print(heap)
        # heap.sort(reverse=True)
        # result = []
        # while heap:
        #     curr = heappop(heap)
        #     result.append(-1*curr[1])
        
        # return result
