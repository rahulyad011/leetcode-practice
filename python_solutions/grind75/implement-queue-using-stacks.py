class MyQueue:
    """
    Idea: the idea is simple here we focus all the work in the push operation
    at time of push we first take all the elements out in a temp stack and then
    insert new element in the main stack and then push all elements from temp to main
    """
    
    def __init__(self):
        self.temp_stack = []
        self.main_stack = []

    def push(self, x: int) -> None:
        # move all elements out of the main stack to put new element at the start of stack
        while self.main_stack:
            curr = self.main_stack.pop()
            self.temp_stack.append(curr)
        # now append the new element
        self.main_stack.append(x)
        #now move back all the other element to restore the existing order
        while self.temp_stack:
            curr = self.temp_stack.pop()
            self.main_stack.append(curr)

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return not len(self.main_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()