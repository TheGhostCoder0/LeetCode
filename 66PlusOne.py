class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            reverse = list(reversed(digits))
            for i in range(len(reverse)):
                if reverse[i] != 9:
                    reverse[i] += 1
                    break
                else:
                    reverse[i] = 0

            if reverse[-1] == 10 or reverse[-1] == 0:
                reverse[len(digits) - 1] = 0
                reverse.append(1)
            return list(reversed(reverse))
                    

            
