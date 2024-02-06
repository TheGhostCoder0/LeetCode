class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        middles = []
        l = []
        for char in s:
            l.append(char)
        
        for char in l:
            if (l.count(char) % 2) == 1 and (char not in middles):
                middles.append(char)
            elif (l.count(char) % 2) == 0:
                continue
        
        if len(middles) > 1:
            return False
        return True
            

