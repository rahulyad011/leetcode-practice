from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Simple count problem, just check if letters required in 
        ransomNote are available in magazine or not
        """
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        for item in ransomCount.items():
            if magazineCount[item[0]]<item[1]:
                return False
        return True