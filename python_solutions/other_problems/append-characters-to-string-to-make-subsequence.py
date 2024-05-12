# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence

"""Solution: 
straight forward compare the character matching in sequence, as sequence reamins the same in subsequence.
Question says what to append at the end of s, note this.
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length_t = len(t)
        index_t = 0
        for i in range(len(s)):
            if s[i]==t[index_t]:
                index_t+=1
            if index_t == length_t:
                return 0
        if index_t:
            return length_t-index_t
        else:
            return length_t