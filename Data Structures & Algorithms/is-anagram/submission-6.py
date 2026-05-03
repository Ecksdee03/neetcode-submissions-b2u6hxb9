class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict_s = Counter(s)
        char_dict_t = Counter(t)
        if len(char_dict_t) != len(char_dict_s):
            return False
        for ch in char_dict_s:
            if ch not in char_dict_t:
                return False
            if char_dict_s[ch] != char_dict_t[ch]:
                return False
        return True
            
        