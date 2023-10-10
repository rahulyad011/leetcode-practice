# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        max_length = 1
        if len(s)<=1:
            return len(s)
        l = 0
        r = 0
        while l <= r and r < len(s):
            char = s[r]
            if char not in count:
                count[char]=r
                max_length = max(max_length, r-l+1)
            else:
                if count[char] >= l:
                    l = count[char]+1
                else:
                    max_length = max(max_length, r-l+1)
                count[char]=r
            r+=1
        return max_length
