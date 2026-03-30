class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        otherNum = 0
        result = []
        tempArr = {}
        for i in range(len(nums)):
            otherNum = target - nums[i]
            if otherNum not in tempArr:
                tempArr[nums[i]] = i
            else:
                result.append(tempArr[otherNum])
                result.append(i)
                return result  
        return result          