class Solution:
    def binary_search(self, A: List[int], s: int, f: int, x: int) -> int:
        if s > f:
            return -1
        m = (s + f) // 2
        if A[m] == x:
            return m
        elif A[m] > x:
            return self.binary_search(A, s, m - 1, x)
        else: 
            return self.binary_search(A, m + 1, f, x)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
