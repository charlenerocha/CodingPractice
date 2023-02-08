class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        myStr = str(x)
        left, right = 0, len(myStr) - 1

        while left < right:
            if myStr[left] != myStr[right]:
                return False
            left += 1
            right -= 1
        
        return True