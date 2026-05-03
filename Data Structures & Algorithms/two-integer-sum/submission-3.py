class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_mapping = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in pair_mapping:
                return [pair_mapping[other], i]
            pair_mapping[nums[i]] = i
        return -1
        