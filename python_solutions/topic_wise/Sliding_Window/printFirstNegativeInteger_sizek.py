# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab


#User function Template for python3

from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    l = 0
    r = 0
    queue = deque()
    result = []
    while r < N:
        if A[r]<0:
            queue.append((A[r], r))
        if (r-l+1) == K:
            if queue:
                neg = queue[0]
                result.append(neg[0])
                if neg[1] == l:
                    queue.popleft()
            else:
                result.append(0)
            l+=1
        r+=1
    return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends