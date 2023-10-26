class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        map = {}
        max_len = 0
        for r in range(len(s)):
            # duplicate outside of current window
            if s[r] in map:
                if map[s[r]] >= l:
                    l = map[s[r]]+1
            map[s[r]]=r
            max_len = max(max_len, r-l+1)
        return max_len