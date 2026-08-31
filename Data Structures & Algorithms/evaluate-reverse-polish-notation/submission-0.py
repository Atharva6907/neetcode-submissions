class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == '+':
                stk.append(stk.pop() + stk.pop())
            elif token == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b - a) # b is the left operand
            elif token == '*':
                stk.append(stk.pop() * stk.pop())
            elif token == '/':
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b / a)) # b is the left operand
            else:
                stk.append(int(token))
        return stk[0]
        