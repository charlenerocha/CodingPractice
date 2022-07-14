class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == t:
            return True
        elif '#' not in s and '#' not in t:
            return False
        
        i = 0
        
        while i < len(s):
            if s[i] == '#':
                s = s[:i] + s[(i+1):]
                if i - 1 >= 0:
                    s = s[:i - 1] + s[(i):]
                    i = i - 1
            else:
                i = i + 1        
        
        i = 0
        
        while i < len(t):
            if t[i] == '#':
                t = t[:i] + t[(i+1):]
                if i - 1 >= 0:
                    t = t[:i - 1] + t[(i):]
                    i = i - 1
            else:
                i = i + 1 

        return s == t