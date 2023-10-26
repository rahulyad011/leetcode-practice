# https://leetcode.com/problems/last-visited-integers/description/
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        index_map = {}
        result = []
        stack = []
        item = ""
        cnt = 0
        for word in words:
            if word == "prev":
                cnt+=1
                if not stack:
                    result.append(-1)
                else:
                    if cnt <= len(stack):
                        item = stack[-(cnt)]
                    else:
                        item = -1
                    result.append(item)
            else:
                cnt = 0
                stack.append(int(word))
        return result