class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # using the binary search approach, rather than merging the arrays, I will try to partition them
        # by adjusting the partitions, I'll get a better estimate of the "middle value"

        totalLength = len(nums1) + len(nums2)
        mid = int(totalLength / 2)

        # [1, 2, 3, 4, 5]
        # [3, 4, 5, 6]
        # totalLength = 9 & mid = 4

        i = int(len(nums1) / 2)     # tracks nums1 left partition
        j = mid - i                 # tracks nums2 left partition

        while True:
            # find values of partitions
            if i < len(nums1):  r1 = nums1[i]
            else:               r1 = float("infinity")
            
            if j < len(nums2):  r2 = nums2[j]
            else:               r2 = float("infinity")
            
            if i - 1 >= 0:      l1 = nums1[i - 1] 
            else:               l1 = float("-infinity")
            
            if j - 1 >= 0:      l2 = nums2[j - 1] 
            else:               l2 = float("-infinity")

            # if the partitions are created accurately
            if l1 <= r2 and l2 <= r1:
                if totalLength % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return min(r1, r2)
            elif l1 > r2:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1


