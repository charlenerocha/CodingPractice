class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ind1 = m-1
        ind2 = n-1
        merged = m+n-1
        print(ind1,ind2,merged)
        
        while(ind1 >= 0 and ind2 >= 0 and merged >= 0):
            if(nums1[ind1] > nums2[ind2]):
                nums1[merged] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[merged] = nums2[ind2]
                ind2 -= 1
            merged -= 1
        
        if(ind1 >= 0):
            nums1[0:merged+1] = nums1[0:ind1+1]
        elif(ind2 >= 0):
            nums1[0:merged+1] = nums2[0:ind2+1]