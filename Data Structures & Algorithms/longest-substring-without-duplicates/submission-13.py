class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dedup = set()
        left = 0
        length = 0
        for r in range(len(s)):
            while s[r] in dedup:
                dedup.remove(s[left])
                left += 1
            dedup.add(s[r])
            length = max(length,r - left + 1)
        return length
