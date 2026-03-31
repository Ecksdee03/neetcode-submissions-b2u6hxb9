class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            other = - nums[i]
            while l < r:
                if nums[l] + nums[r] > other:
                    r -= 1
                elif nums[l] + nums[r] < other:
                    l += 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return [list(i) for i in res]

                
