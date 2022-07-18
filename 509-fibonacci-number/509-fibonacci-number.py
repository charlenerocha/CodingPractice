class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            return n
        
        prev, cur = 0, 1
        
        for i in range(n - 1):
            temp = prev
            prev = cur
            cur = cur + temp
            
        return cur