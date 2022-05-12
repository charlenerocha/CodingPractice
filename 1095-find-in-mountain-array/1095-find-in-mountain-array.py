# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        
        left, right=0, mountain_arr.length()-1
        peak=-1
        
        while left<=right:
            mid=(left+right)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                left=mid+1
            else:
                peak=mid
                right=mid-1
        
        left, right=0,peak
        while left<=right:
            mid=(left+right)//2
            if mountain_arr.get(mid)==target:
                return mid
            elif mountain_arr.get(mid)<target:
                left=mid+1
            else:
                right=mid-1
                
        left, right=peak, mountain_arr.length()-1
        while left<=right:
            mid=(left+right)//2
            if mountain_arr.get(mid)==target:
                return mid
            elif mountain_arr.get(mid)>target:
                left=mid+1
            else:
                right=mid-1
                
        return -1
        