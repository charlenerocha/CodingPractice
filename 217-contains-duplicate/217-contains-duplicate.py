class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        for i in nums:
            if(i in d):
                return 1
            else:
                d[i]= i
                
        return 0
        