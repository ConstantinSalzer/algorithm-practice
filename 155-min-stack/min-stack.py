class MinStack:

    def __init__(self):
        self.stack = []
        self.minelement = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minelement:
            self.minelement.append(value)
        elif (self.minelement[len(self.minelement)-1]<value):
            self.minelement.append(self.minelement[len(self.minelement)-1])
        else:
            self.minelement.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minelement.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minelement[len(self.minelement)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()