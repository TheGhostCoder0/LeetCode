class Solution:
    def addDigits(self, num: int) -> int:
        num_string = str(num)
        sum = 0
        while len(num_string) != 1:
            sum = 0
            for char in num_string:
                sum += int(char)
            num_string = str(sum)
            
        return int(num_string)
