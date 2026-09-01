class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for i in range(len(position)):
            lst.append((position[i], speed[i]))
        lst.sort(reverse = True)
        times = []
        for i in range(len(lst)):
            times.append((target - lst[i][0]) / lst[i][1])
        stk = []
        for i in range(len(lst)):
            if not stk:
                stk.append(times[i])
            elif times[i] > stk[-1]:
                stk.append(times[i])
        return len(stk)

        