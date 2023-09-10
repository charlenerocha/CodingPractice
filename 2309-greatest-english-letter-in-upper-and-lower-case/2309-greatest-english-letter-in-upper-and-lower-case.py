class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(k for k in s)
        checked = set()
        greatest = ""
        
        for letter in seen:
            if letter not in checked and letter.upper() in seen and letter.lower() in seen and letter > greatest:
                greatest = letter
            checked.add(letter)
            
        return greatest.upper()