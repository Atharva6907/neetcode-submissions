class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        ans = ""
        lauda = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for char in s:
            if char == ']':
                temp = ""
                while stk[-1] != '[':
                    a = stk.pop()
                    temp = a + temp
                stk.pop()
                reps = ""
                while stk and stk[-1] in lauda:
                    sing = stk.pop()
                    reps = sing + reps
                b = int(reps)
                x = ""
                for i in range(b):
                    x += temp
                stk.append(x)
            else:
                stk.append(char)
        return "".join(stk)