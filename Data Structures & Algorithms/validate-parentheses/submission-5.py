class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chDict = {')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in chDict and stack:
                latestCh = stack.pop()
                if latestCh != chDict[s[i]]:
                    return False
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        return True