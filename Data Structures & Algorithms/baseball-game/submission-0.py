class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for char in operations:
            if char == '+':
                lst.append(lst[-1] + lst[-2])
            elif char == 'D':
                lst.append(2*lst[-1])
            elif char == 'C':
                lst.pop()
            else:
                lst.append(int(char))
        ans = 0
        for i in lst:
            ans += i
        return ans
        