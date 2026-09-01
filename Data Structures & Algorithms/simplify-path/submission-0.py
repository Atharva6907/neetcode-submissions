class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        paths = path.split("/")
        for char in paths:
            if char == "..":
                if stk:
                    stk.pop()
            elif char != "" and char != ".":
                stk.append(char)
        return "/" + "/".join(stk) 

        