class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:
        first lower the string then create a string with only only alnum values
        or swip the comparision when left or right are alnum
        """
        clean_s = ""
        for char in s.lower():
            if char.isalnum():
                clean_s += char
        l = 0
        r = len(clean_s)-1
        while l<r:
            if clean_s[l] != clean_s[r]:
                return False
            else:
                l+=1
                r-=1
        return True