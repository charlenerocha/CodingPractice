class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #recursive solution
        
        def fibNum(n):
            if n == 0:
                return 0

            if n == 1:
                return 1

            return fibNum(n - 1) + fibNum(n - 2)
        
        return fibNum(n)