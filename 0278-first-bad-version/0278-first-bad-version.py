# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # creates a "mountain effect" ex. FFTTT
        # we can use a binary search method to find the first occurance of T!

        left, right = 1, n

        while left < right:
            mid = int((left + right) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return right