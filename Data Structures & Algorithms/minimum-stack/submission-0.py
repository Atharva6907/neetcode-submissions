class MinStack:

    def __init__(self):
        self.stk = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.mini) == 0 or self.mini[-1] >= val:
            self.mini.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        if self.mini[-1] == val:
            self.mini.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]

        
