class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        max_count = 0
        left = 0
        for i in range(len(s)):
            while s[i] in ch_set:
                ch_set.remove(s[left])
                left += 1           
            ch_set.add(s[i])
            max_count = max(i-left+1, max_count)
        return max_count
        