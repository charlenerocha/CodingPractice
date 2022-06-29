class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        myNum = 0
        neg = True if x < 0 else False
        x = x * -1 if neg else x
        
        while x != 0:
            myNum = (myNum * 10) + (x % 10)
            x = x / 10
        
        if myNum >= 2147483648:
            return 0
        
        return myNum * -1 if neg else myNum