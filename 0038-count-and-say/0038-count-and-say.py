class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        prev = self.countAndSay(n-1)
        curr = prev[0]
        count = 0
        final = ""
        for num in prev:
            if num != curr:
                final += (str(count) + curr)
                curr = num
                count = 1
            else:
                count += 1
        final += (str(count) + str(curr))
            
        return final