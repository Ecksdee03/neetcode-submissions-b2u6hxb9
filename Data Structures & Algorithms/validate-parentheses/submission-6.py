class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chDict = {')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in chDict and stack:
                if stack[-1] != chDict[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        return True