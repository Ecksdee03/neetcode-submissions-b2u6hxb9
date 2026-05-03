class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        print(dedup)
        if len(nums) == len(dedup):
            return False
        return True
        