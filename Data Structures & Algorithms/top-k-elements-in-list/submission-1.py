class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        return [item for item, count in numCounter.most_common(k)]
        