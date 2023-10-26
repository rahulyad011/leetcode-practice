import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        learning 1(important):
        the functions s.lower() and s.isalnum() are not actually functions
        there are String class methods so need to be called as s.method_name()
        instead of method_name(s)
        """

        """
        solution1: don't clean just skip the nonalnum and compare with 
        two pointer for palindrome
        """
        # left = 0
        # right = len(s)-1
        # l_check, r_check = '', ''
        # while left < right:
        #     if s[left].isalnum():
        #         l_check = s[left].lower()
        #     else:
        #         left+=1
        #         continue
        #     if s[right].isalnum():
        #         r_check = s[right].lower()
        #     else:
        #         right-=1
        #         continue
        #     # print(l_check, r_check)
        #     if l_check != r_check:
        #         return False
        #     else:
        #         left+=1
        #         right-=1
        # return True

        """
        solution2: first clean the string and then compare for palindrome
        """
        s_lowered = s.lower()
        s_clean = ""
        # for char in s_lowered:
        #     if char.isalnum():
        #         s_clean += char
        s_clean = s_lowered
        l = 0
        r = len(s_clean)-1
        while l < r:
            if s_clean[l].isalnum() and s_clean[r].isalnum():
                if s_clean[l] != s_clean[r]:
                    return False
                l+=1
                r-=1
            else:
                if not s_clean[l].isalnum():
                    l+=1
                if not s_clean[r].isalnum():
                    r-=1
        return True