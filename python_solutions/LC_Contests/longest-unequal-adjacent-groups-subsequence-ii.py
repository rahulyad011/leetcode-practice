# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def check_words(word1, word2):
            if len(word1)!=len(word2):
                return False
            cnt = 0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    cnt+=1
                if cnt>1:
                    return False
            if cnt<=1:
                return True
            else:
                return False
        
        dp = [1 for i in range(n)]
        prev_ind = [-1 for i in range(n)]
        max_seq = (1, 0) # (length, index)

        for i in range(1, n):
            for j in range(0, i):
                if groups[i]!=groups[j] and check_words(words[i], words[j]):
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        prev_ind[i] = j
            if dp[i] > max_seq[0]:
                max_seq = (dp[i], i)
        
        result = []
        index = max_seq[1]
        #index is the last index of the longest sequence now we go back using prev_ind list
        while index !=-1:
            result.append(words[index])
            index = prev_ind[index]
        return reversed(result)

        """try to write a knapsack like recursive solution some other day"""
        # def ls(n):
        #     if n<=1:
        #         return n
        #     if groups[n-1]!=groups[n-2] and check_words(words[n-1], words[n-2]):
                



                    



        

        