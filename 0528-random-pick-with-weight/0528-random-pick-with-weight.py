class Solution:

    def __init__(self, w: List[int]):
        self.probability = []
        self.totalSum = 0
        for val in w:
            self.totalSum += val
            self.probability.append(self.totalSum)
        print(self.probability)
        
    def pickIndex(self) -> int:
        randSeed = self.totalSum * random.random()
        
        for i, val in enumerate(self.probability):
            if randSeed <= val:
                return i
            
        return 0
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()