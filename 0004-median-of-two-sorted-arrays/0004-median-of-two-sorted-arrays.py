class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # SECOND ATTEMPT
        
        # unoptimized: combine both lists in a sorted order, traverse to find the median
        # optimized: find the combined left side, then you have your median!!

        # initial guess
        totalLength = len(nums1) + len(nums2)
        medianSpot = totalLength / 2

        median1 = (len(nums1) / 2) - 1
        median2 = (medianSpot - median1) - 2

        # until left interval is found correctly
        while True:
            l1 = nums1[median1] if (median1 >= 0 and median1 < len(nums1)) else float("-infinity")
            l2 = nums2[median2] if (median2 >= 0 and median2 < len(nums2)) else float("-infinity")
                
            r1 = nums1[median1 + 1] if (median1 + 1 >= 0 and median1 + 1 < len(nums1)) else float("infinity")
            r2 = nums2[median2 + 1] if (median2 + 1 >= 0 and median2 + 1 < len(nums2)) else float("infinity")

            if l1 <= r2 and l2 <= r1:
                # if there are two in the middle
                if totalLength % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return min(r1, r2)
            # adjust interval
            elif l1 > r2:
                median1 -= 1
                median2 += 1
            else:
                median1 += 1
                median2 -= 1