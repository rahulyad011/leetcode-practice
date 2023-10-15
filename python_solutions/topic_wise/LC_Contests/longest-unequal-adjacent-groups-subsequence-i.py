class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        indexes = [0]
        result = [words[0]]
        for i in range(1, n):
            if groups[i-1]!=groups[i]:
                indexes.append(i)
                result.append(words[i])
        return result