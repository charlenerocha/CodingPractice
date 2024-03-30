class Solution:
    
    def __init__(self):
        self.permutations = []
        self.nums = []
    
    def backtrack(self, path, used: List[bool]):
        if len(path) == len(used):
            self.permutations.append(path[:])
            return
        
        for i in range(len(used)):
            if not used[i]:
                path.append(self.nums[i])
                used[i] = True
                self.backtrack(path, used)
                used[i] = False
                path.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack([], [False]*len(nums))
        return self.permutations