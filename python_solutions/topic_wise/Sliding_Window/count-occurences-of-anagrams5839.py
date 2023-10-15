# https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

"""Important Learning how to delete a element from a Counter/Dict --> del dict_map[element]"""

#User function Template for python3
from collections import Counter

class Solution:
    def search(self,pat, txt):
        # code here
        text_map_k = Counter("")
        word_map = Counter(pat)
        
        k = len(pat)
        
        l = 0
        r = 0
        cnt = 0
        while r<len(txt):
            text_map_k[txt[r]] += 1
            if r-l+1 == k:
                if text_map_k == word_map:
                    cnt+=1
                text_map_k[txt[l]]-=1
                if text_map_k[txt[l]] == 0:
                    # this is a important syntax
                    del text_map_k[txt[l]]
                l+=1
            r+=1
        return cnt
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends