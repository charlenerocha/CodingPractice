class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return
        
        finalString = ""
        start, end = 0, 0
        
        while end < len(s):
            while end < len(s) and s[end] != " ":
                end = end + 1
            
            tempString = s[start:end]
            tempString = tempString[len(tempString)::-1]
            
            finalString = finalString + " " + tempString
            start = end + 1
            end = end + 1
            
        return finalString[1:]
            