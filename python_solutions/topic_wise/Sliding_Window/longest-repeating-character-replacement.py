# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = defaultdict(int)
        l = 0
        r = 1
        if len(s)<=1:
            return len(s)
        curr_max = 0
        char_map[s[l]] += 1
        while r<len(s):
            char_map[s[r]]  += 1
            curr_max = max(curr_max, char_map[s[r]])
            #window is valid only
            curr_size = (r-l+1)
            if curr_size - curr_max > k:
                char_map[s[l]]-=1
                l+=1
            r+=1
        r-=1
        return r-l+1