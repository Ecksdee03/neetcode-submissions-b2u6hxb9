class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        substr = set()
        left = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[r])
            length = max(length, r-left+1)
        return length

