class MyStack:

    def __init__(self):
        self.stk = []
        self.sz = 0

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.sz += 1
        for _ in range(self.sz-1):
            self.stk.append(self.stk.pop(0))

    def pop(self) -> int:
        self.sz -= 1
        return self.stk.pop(0)
        

    def top(self) -> int:
        return self.stk[0]

    def empty(self) -> bool:
        return self.sz == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()