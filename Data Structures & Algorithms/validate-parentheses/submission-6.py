class Solution:
    def isValid(self, s: str) -> bool:
        charDict = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for c in s:
            if c in charDict:
                stack.append(c)
            elif stack and charDict[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return not stack