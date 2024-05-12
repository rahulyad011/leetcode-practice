# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.minimums = []
        self.mainstack = []

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if self.minimums:
            if self.minimums[-1] >= val:
                self.minimums.append(val)
        else:
            self.minimums.append(val)

    def pop(self) -> None:
        curr = self.mainstack.pop()
        if self.minimums and self.minimums[-1] == curr:
            self.minimums.pop()
        return curr

    def top(self) -> int:
        return self.mainstack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()