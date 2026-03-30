class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = "".join(sorted(s))
        t_count = "".join(sorted(t))
        return s_count == t_count