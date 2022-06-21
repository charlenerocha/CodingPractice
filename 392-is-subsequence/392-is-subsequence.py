class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sLen = len(s)
        
        if sLen > len(t):
            return False
        elif sLen == 0:
            return True
        
        sIndex = 0
        
        for i, letter in enumerate(t):
            if letter == s[sIndex]:
                sIndex += 1
            if sIndex >= sLen:
                return True
            
        return False