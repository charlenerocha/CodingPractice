class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def multiply(base, power):
            if power == 0:
                return 1
            if power == 1:
                return base
            if power == 2:
                return base * base

            extra = 1
            
            if power % 2 == 1:
                extra = base
            
            return extra * multiply(base * base, power/2)
        
        myNum = multiply(x, abs(n))
            
        return myNum if n > 0 else 1/myNum