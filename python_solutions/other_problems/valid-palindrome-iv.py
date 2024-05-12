# https://leetcode.com/problems/valid-palindrome-iv

"""Solution:
Simple two pointer solution
"""

class Solution:
    def makePalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s)-1
        change_count = 0
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                change_count += 1
            left_index +=1
            right_index -=1
            if change_count > 2:
                return False
        return True
        