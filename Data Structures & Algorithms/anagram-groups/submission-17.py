class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print(res)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord("a")] += 1
            res[tuple(count)].append(word)
        print(list(res.values()))
        return list(res.values())