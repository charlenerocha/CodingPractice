class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        maxSum = 0
        
        # pick all 1's
        numPicked = min(numOnes, k)
        maxSum += sum(1 for i in range(numPicked))
        k = max(k - numPicked, 0)
        
        # pick all 0's
        numPicked = min(numZeros, k)
        k = max(k - numPicked, 0)
        
        # pick all -1's
        numPicked = min(numNegOnes, k)
        maxSum -= sum(1 for i in range(numPicked))
        k = max(k - numPicked, 0)
        
        return maxSum