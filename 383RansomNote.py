class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = []
        for letter in magazine:
            letters.append(letter)
        
        for letter in ransomNote:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
