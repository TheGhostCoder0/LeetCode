class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        bitSetCount = 0
        position = 0

        for i in range(32):  
            if n & (1 << i):
                bitSetCount += 1
                position = i

        return bitSetCount == 1 and position % 2 == 0
