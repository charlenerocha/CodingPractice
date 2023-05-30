class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # "   fly me   to   the moon  "
        
        # where the last letter of the last word is
        lastWordIndex = len(s) - 1
        
        while s[lastWordIndex] == " ":
            if lastWordIndex < 0:
                return 0
            lastWordIndex -= 1
            
        lastWordCounter = 0
        i = lastWordIndex
        while s[i] != " " and i >= 0:
            lastWordCounter += 1
            i -= 1
        
        return lastWordCounter
    