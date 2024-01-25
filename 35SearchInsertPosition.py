class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        i = 1
        j = len(nums) - 1
        midIndex = (i + j) // 2
        while i <= j:
            midIndex = (i + j) // 2
            midVal = nums[midIndex]
            if midVal == target:
                return midIndex
            elif midVal < target:
                i = midIndex + 1
            else:
                j = midIndex - 1
        return midIndex + 1 if target > nums[midIndex] else midIndex
