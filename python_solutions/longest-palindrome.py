from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        result = 0
        middle_pick = 0
        for item in char_count.items():
            if item[1]%2==0:
                result += item[1]
            else:
                if middle_pick:
                    result += (item[1]-1)
                else:
                    result += item[1]
                    middle_pick=1     
        return result
            