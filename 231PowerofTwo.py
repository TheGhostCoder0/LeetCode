class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        val = math.floor(math.log(n, 2)) + 1
        bitSetCount = 0
        for i in range(val):
            if (n & (1 << i)) != 0:
                bitSetCount += 1

        return bitSetCount == 1
