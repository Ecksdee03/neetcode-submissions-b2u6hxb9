class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = {}
        secondDict = {}
        for i in s:
            if i not in firstDict:
                firstDict[i] = 1
            else:
                addCh = firstDict[i] + 1
                firstDict[i] = addCh
        for j in t:
            if j not in firstDict:
                return False
            else:
                if j not in secondDict:
                    secondDict[j] = 1
                else:
                    addCh = secondDict[j] + 1
                    secondDict[j] = addCh
        for ch in firstDict:
            if firstDict.get(ch) != secondDict.get(ch):
                return False
        return True
            
        