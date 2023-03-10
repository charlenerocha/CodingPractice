class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # "   fly me   to   the moon  "
        
        length_last_word = 0
        seen_word = False
        index = len(s) - 1
        
        while index >= 0 and (seen_word == False or (seen_word and s[index] != " ")):
            if s[index] != " ":
                seen_word = True
                length_last_word += 1
            index -= 1
            
        return length_last_word