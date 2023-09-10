class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(k for k in s)
        greatest = ""
        
        for letter in seen:
            if letter.upper() in seen and letter.lower() in seen and letter > greatest:
                greatest = letter
            
        return greatest.upper()