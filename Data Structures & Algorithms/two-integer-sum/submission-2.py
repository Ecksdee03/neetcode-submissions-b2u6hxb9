class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempArr = {}
        for i in range(len(nums)):
            otherNum = target - nums[i]
            if otherNum in tempArr:
                return [tempArr[otherNum],i]  
            tempArr[nums[i]] = i
        return []   