class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num,0) + 1
            if numCount[num] > len(nums)/2:
                return num