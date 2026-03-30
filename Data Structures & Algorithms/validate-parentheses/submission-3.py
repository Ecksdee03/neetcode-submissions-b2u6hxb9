class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chDict = {')':'(','}':'{',']':'['}
        if len(s) == 0 or len(s)%2 != 0 or s[0] in chDict:
            return False
        for i in range(len(s)):
            if s[i] in chDict and len(stack)>0:
                latestCh = stack.pop()
                if latestCh != chDict[s[i]]:
                    return False
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        return True