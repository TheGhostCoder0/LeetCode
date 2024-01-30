class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_number = bin(n)[2:]

        flipped_binary = ''.join('0' if bit == '1' else '1' for bit in binary_number)

        flipped_number = int(flipped_binary, 2)

        return flipped_number
