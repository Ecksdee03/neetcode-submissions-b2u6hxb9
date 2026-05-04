class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        freq = defaultdict(list)
        for (num,cnt) in count.items():
            freq[cnt].append(num)

        for j in range(len(nums), 0, -1):
            for num in freq[j]:
                res.append(num)
                if len(res) == k:
                    return res