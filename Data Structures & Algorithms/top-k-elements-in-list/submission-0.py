class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        output = []
        while k > 0:
            max_item_tuple = numCounter.most_common(1)
            if max_item_tuple:
                item_to_remove = max_item_tuple[0][0]
                output.append(item_to_remove)
                del numCounter[item_to_remove]
            k -= 1
        return output
        