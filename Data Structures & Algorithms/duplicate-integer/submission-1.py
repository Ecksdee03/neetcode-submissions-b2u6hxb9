class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNumbers = []
        for num in nums:
            if num not in uniqueNumbers:
                uniqueNumbers.append(num)
            else:
                return True
        return False