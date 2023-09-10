class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # apply a sliding window that ends when r == len(nums) - 1
        subsequence_array = nums[:k]
        min_subsequence = min(subsequence_array)
        
        for new in range(k, len(nums)):
            if nums[new] > min_subsequence:
                subsequence_array.remove(min_subsequence)
                subsequence_array.append(nums[new])
                min_subsequence = min(subsequence_array)
            
        return subsequence_array