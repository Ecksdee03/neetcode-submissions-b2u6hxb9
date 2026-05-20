class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        hmap = {}
        for r in range(len(s)):
            if s[r] in hmap:
                left = max(left,hmap[s[r]] + 1)
            hmap[s[r]] = r
            print(left)
            length = max(length, r-left+1)
        return length
        