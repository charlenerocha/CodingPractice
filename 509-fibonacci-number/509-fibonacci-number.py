class Solution(object):
    fibs = {0:0, 1:1}
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in self.fibs:
            return self.fibs[n]
        
        self.fibs[n] = self.fibs[n - 1] + self.fibs[n - 2]
        
        return self.fibs[n]
            