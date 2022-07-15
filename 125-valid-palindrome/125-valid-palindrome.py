class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        left, right = 0, len(s) - 1
        
        while left < right:
            print s[left]
            print s[right]
            
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left = left + 1
                right = right - 1
            else:
                if s[left].isalnum() == False:
                    left = left + 1
                if s[right].isalnum() == False:
                    right = right - 1
                    
        return True