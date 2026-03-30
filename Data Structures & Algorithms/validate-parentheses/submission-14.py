class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chDict = {')':'(', '}':'{', ']': '['}
        for i in range(len(s)):
            if stack and s[i] in chDict:
                if chDict[s[i]] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        return True 
                