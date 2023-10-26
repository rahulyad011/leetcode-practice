class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        solution: to manage the empty string better take zero for those values
        string  doesn't have a direct reverse function in python so add new at the start
        instead of reversing the string start sum from the end 
        """
        n = len(a)-1
        m = len(b)-1
        carry = 0
        result = ""
        while n>=0 or m>=0:
            first = 0
            second = 0
            if n>=0:
                first = int(a[n])
                n-=1
            if m>=0:
                second = int(b[m])
                m-=1
            sumb = (first+second+carry)%2
            carry = (first+second+carry)//2
            result = str(sumb)+result
        if carry:
            result = str(carry)+result
        return result