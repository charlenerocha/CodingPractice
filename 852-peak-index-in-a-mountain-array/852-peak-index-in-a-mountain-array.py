class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right=0, len(arr)-1
        peak=-1
        
        while left<=right:
            mid=(left+right)//2
            if arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                peak=mid
                right=mid-1
        
        return peak