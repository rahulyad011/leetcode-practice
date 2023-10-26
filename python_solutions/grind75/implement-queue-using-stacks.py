class MyQueue:

    """
    Idea: the idea is simple here we focus all the work in the push operation
    at time of push we first take all the elements out in a temp stack and then
    insert new element in the main stack and then push all elements from temp to main
    """
    stack_in = None
    stack_temp = None

    def __init__(self):
        self.stack_in = []
        self.stack_temp = []

    def push(self, x: int) -> None:
        # this is the main logic
        # stack_in is our main stack so we maintain that
        while self.stack_in:
            out = self.stack_in.pop()
            self.stack_temp.append(out)
        self.stack_in.append(x)
        while self.stack_temp:
            out_t = self.stack_temp.pop()
            self.stack_in.append(out_t)

    def pop(self) -> int:
        out = self.stack_in.pop()
        return out

    def peek(self) -> int:
        return self.stack_in[-1]

    def empty(self) -> bool:
        return not len(self.stack_in)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()