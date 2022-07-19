class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0
        
        find = 0
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i : len(needle) + i] == needle:
                return i
            
        return -1
            