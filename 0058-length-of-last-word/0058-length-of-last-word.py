class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        isCharSeen = False
        lastWordCount = 0
        i = len(s) - 1
        
        while i >= 0:
            if isCharSeen == True:
                if s[i] == " ":
                    return lastWordCount
                else:
                    lastWordCount += 1
            else:
                if s[i] != " ":
                    isCharSeen = True
                    lastWordCount += 1
                
            i-=1
        
        return lastWordCount
    