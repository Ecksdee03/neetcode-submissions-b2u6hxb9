class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml, sumr = 0,0
        for i in range(len(nums)):
            suml = sum(nums[0:i])
            sumr = sum(nums[i+1:len(nums)])
            print(suml, sumr)
            if suml == sumr:
                return i
        return -1
        