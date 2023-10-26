# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        "Brute ofr O(n2) solution" 
        min_len = 1000
        result = []
        final_result = []
        for i in range(len(s)):
            sum_now = 0
            for j in range(i, len(s)):
                sum_now += int(s[j])
                if sum_now == k:
                    if (j-i+1)<min_len:
                        min_len = j-i+1
                        result.append(s[i:j+1])
                    else:
                        if (j-i+1) == min_len:
                            result.append(s[i:j+1])
                    break
        for item in result:
            if len(item) == min_len:
                final_result.append(item)
        final_result.sort()
        if final_result:
            return final_result[0]
        else:
            return ""


        """Sliding Window Solution Try again later"""        
        # l = 0
        # r = 0
        # curr_sum = 0
        # result = []
        # min_len = 0
        # while r < len(s):
        #     curr_sum += int(s[r])
        #     if curr_sum == k:
        #         if not result:
        #             result.append(s[l:r+1])
        #         else:
        #             if len(result[0])>(r-l+1):
        #                 result = []
        #                 result.append(s[l:r+1])
        #             if len(result[0])==(r-l+1):
        #                 result.append(s[l:r+1])
        #         while l < r:
        #             curr_sum -= int(s[l])
        #             l+=1
        #     # if curr_sum >= k
        #     r+=1
        # while l < r:
        #     curr_sum -= int(s[r])
        #     if curr_sum == k:
        #         if not result:
        #             result.append(s[l:r+1])
        #         else:
        #             if len(result[0])>(r-l+1):
        #                 result = []
        #                 result.append(s[l:r+1])
        #             if len(result[0])==(r-l+1):
        #                 result.append(s[l:r+1])
        #         curr_sum -= int(s[l])
        #     l+=1
        # print(result)
        # result.sort(reverse=True)
        # if result:
        #     mins = result[0]
        # else:
        #     mins = ""
        # for item in result:
        #     if len(item) < len(mins):
        #         mins = item
        # return mins
                