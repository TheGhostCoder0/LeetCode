class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        l = []
        if lower < nums[0]:
            l.append([lower, nums[0] - 1])
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                l.append([nums[i] + 1, nums[i + 1] - 1])
        if upper > nums[-1]:
            l.append([nums[-1] + 1, upper])
        return l
