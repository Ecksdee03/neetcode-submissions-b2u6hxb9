class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_mapping = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            words_mapping[tuple(count)].append(word)
        return list(words_mapping.values())